# PLAN — đưa 16 stack repo-lồng vào quản lý của repo selfhost

Lập ngày 2026-08-09. Đánh dấu `[x]` khi làm xong + đã verify.

## Vấn đề

`dockge/stacks/` có 16 thư mục là git repo riêng (có `.git` bên trong) nhưng
repo cha không khai submodule. Git cha **bỏ qua im lặng**: `git status` hiện
chúng ở `??`, `git add -A` không nuốt được nội dung, nên clone `selfhost` về
máy mới là **thiếu hẳn 16 stack**.

15/16 có compose file, tức stack chạy được. Nghiêm trọng nhất:
**`server-control` đang CHẠY** (container `serverui`) mà repo cha không giữ gì.

## Hiện trạng đã khảo sát

Tin tốt: cả 16 đều có remote, và **không cái nào có commit chưa push**. Nội
dung lấy lại được từ remote — submodule pin là an toàn.

Tin xấu: **9/16 đang dirty, và thứ bị sửa chính là compose file**:

| Repo | Sửa gì |
|------|--------|
| `server-control` | `M compose.yml` + rác `.compose.yml.swp` |
| `huy-cheatsheet` | `D docker-compose.yml`, `?? compose.yml` (đổi tên cho Dockge) |
| `service-hub` | `D docker-compose.yml`, `?? compose.yml` |
| `stress-wifi` | `D docker-compose.yml` + sửa Makefile, utils/db.go |
| `teleport-setup` | `?? compose.yml`, `?? teleport/` |
| `syncthing` | `M compose.yml`, `?? Pictures/` |
| `mock-server` | `M docker-compose.yml`, Makefile |
| `auto-rename` | `M docker-compose.yml` |
| `sign0z` | 48 file (README + xoá gần hết `deploy/`) |

Submodule chỉ ghi lại **commit hash**, không ghi thay đổi chưa commit. Add
submodule ngay lúc này = pin vào commit KHÔNG chứa compose đang chạy. Clone
máy mới vẫn hỏng, chỉ khác là hỏng âm thầm hơn.

Nên thứ tự bắt buộc: **commit vào repo con TRƯỚC, add submodule SAU**.

## Phân loại

**Repo của mình (11)** — sửa được, push được:
`auto-rename`, `chi-tieu` (finance-management), `gemini-usage-tracker`,
`huy-cheatsheet` (cheatsheet), `mock-server`, `open-webhook`, `server-control`,
`service-hub` (service-portal), `stress-wifi`, `syncthing`, `webhook-tester`

**Clone của bên thứ ba (5)** — không push ngược lên được:
`firecrawl/repo` (mendableai), `sign0z` (SigNoz), `superset` (apache),
`teleport-setup` (auyongjinyoo), `temporalio/docker-compose` (temporalio)

Hai nhóm này xử lý khác nhau — xem Giai đoạn 2 và 3.

---

## Giai đoạn 0 — Dọn rác trước

- [ ] Xoá `dockge/stacks/server-control/.compose.yml.swp` (file swap của vim).
- [ ] Xem `syncthing/Pictures/` (repo 977M) là data hay nhầm chỗ. Nếu là data
      thì thêm vào `.gitignore` của chính repo con, đừng commit.
- [ ] `sign0z` đang xoá gần hết `deploy/` — xác nhận là cố ý hay hỏng dở. Nếu
      không dùng nữa thì cân nhắc xoá hẳn stack thay vì mang theo 84M.

## ĐÃ XONG — 6 submodule sạch (commit fdee3a5)

Sáu repo working tree không lệch, pin commit là đủ tái tạo đúng thứ đang chạy:

- [x] `firecrawl/repo` — mendableai/firecrawl @ `v2.8.0-17-g83676035`
- [x] `gemini-usage-tracker` — nguyenhuy158 @ `heads/main`
- [x] `open-webhook` — nguyenhuy158 @ `heads/main`
- [x] `superset` — apache/superset @ `heads/master`
- [x] `temporalio/docker-compose` — temporalio @ `v1.28.1-1-g3e1faf6`
- [x] `webhook-tester` — nguyenhuy158 @ `heads/main`

Verify đã chạy: `git submodule status` đủ 6, không dấu `-`/`+`; diff staged chỉ
có `.gitmodules` + 6 gitlink, không file nội dung nào lọt vào repo cha.

---

## CÒN LẠI — 10 việc, đánh số theo thứ tự nên làm

Đánh số S1..S10. Mỗi việc: commit vào repo CON trước (nếu dirty), push, rồi mới
`git submodule add` ở repo CHA.

### S1. `server-control` — ƯU TIÊN CAO NHẤT

Đang CHẠY thật (container `serverui`) mà repo cha không giữ gì. Dựng lại máy là
thiếu stack, không có lỗi nào báo.

- [ ] Xoá rác `.compose.yml.swp` (swap file của vim)
- [ ] Commit `M compose.yml` vào `nguyenhuy158/server-control`, push
- [ ] `git submodule add git@github.com:nguyenhuy158/server-control.git dockge/stacks/server-control`

### S2. `chi-tieu` — CÓ SECRET, xử trước khi đụng submodule

Repo con đang **track** `frontend-admin/.env` với `GOOGLE_CLIENT_SECRET` thật
(`GOCSPX-...`). Working tree sạch nên add submodule được ngay, nhưng secret đã
nằm sẵn trong `nguyenhuy158/finance-management`.

- [ ] Rotate Google OAuth client secret ở Google Cloud Console
- [ ] `git rm --cached frontend-admin/.env` trong repo con, thêm `.env` vào
      `.gitignore` của nó, tạo `.env.example`, commit + push
- [ ] `git submodule add git@github.com:nguyenhuy158/finance-management.git dockge/stacks/chi-tieu`

### S3. `huy-cheatsheet` — rename compose

`D docker-compose.yml` + `?? compose.yml` (đổi tên cho Dockge), thêm
`M static/index.html`.

- [ ] Commit cả xoá lẫn thêm trong CÙNG một commit để git nhận ra là rename
- [ ] Push, rồi `git submodule add git@github.com:nguyenhuy158/cheatsheet.git dockge/stacks/huy-cheatsheet`

### S4. `service-hub` — rename compose

`D docker-compose.yml` + `?? compose.yml`. Làm như S3.

- [ ] Commit rename, push
- [ ] `git submodule add git@github.com:nguyenhuy158/service-portal.git dockge/stacks/service-hub`

### S5. `mock-server`

`M Makefile`, `M docker-compose.yml`.

- [ ] Commit, push, add submodule

### S6. `auto-rename`

`M docker-compose.yml`. Repo 19M.

- [ ] Commit, push, add submodule

### S7. `stress-wifi`

`D docker-compose.yml` + `M .gitignore`, `M Makefile`, `M utils/db.go` — lệch cả
code, không chỉ compose. Xem lại từng file trước khi commit.

- [ ] Rà diff, commit, push, add submodule

### S8. `syncthing` — kiểm data trước

Repo 977M, có `?? Pictures/` và `M compose.yml`.

- [ ] Xác định `Pictures/` là data hay để nhầm chỗ. Nếu là data: thêm vào
      `.gitignore` của repo con, KHÔNG commit
- [ ] Commit `compose.yml`, push, add submodule

### S9. `teleport-setup` — clone bên thứ ba, có phần tự viết

Upstream `auyongjinyoo/teleport-setup`, không push ngược được. Local có
`?? compose.yml` và `?? teleport/` do mình thêm — pin submodule sẽ MẤT hai thứ này.

- [ ] Tách phần tự viết ra thư mục thường của repo cha, vd
      `dockge/stacks/teleport-setup-config/`
- [ ] Rồi mới `git submodule add` phần upstream

### S10. `sign0z` — QUYẾT ĐỊNH TRƯỚC, đừng làm vội

48 file lệch, đã xoá gần hết `deploy/`, nặng 84M. Upstream `SigNoz/signoz`.

- [ ] Trả lời: còn dùng không?
      - Không → xoá hẳn stack, gọn hơn nhiều
      - Có → fork lên `nguyenhuy158/signoz`, đổi remote, commit 48 file lệch
        vào fork, rồi đối xử như nhóm repo của mình

## Giai đoạn 4 — Cập nhật tài liệu và quy trình

- [ ] `README.md`: ghi rõ phải clone bằng
      `git clone --recurse-submodules`, hoặc `git submodule update --init
      --recursive` sau khi clone. Thiếu bước này là `dockge/stacks/*` rỗng.
- [ ] Ghi lại luật commit hai bước: sửa stack là commit repo CON trước, push,
      rồi mới commit con trỏ ở repo CHA.

---

## Rủi ro

- **R1. Commit hai bước.** Quên commit con trỏ ở repo cha thì máy khác vẫn kéo
  về commit cũ, không cảnh báo gì. Chi phí cố định của submodule.

- **R2. Clone thiếu.** `git clone` thường ra `dockge/stacks/<ten>` RỖNG. Với
  `server-control` đang chạy thật, dựng lại máy mà quên `--recurse-submodules`
  là thiếu stack mà không có lỗi nào báo.

- **R3. Dirty không được pin.** Submodule chỉ ghi commit hash. Mọi thứ chưa
  commit trong repo con KHÔNG nằm trong repo cha. Đây là lý do Giai đoạn 1 phải
  chạy trước Giai đoạn 2, không được đảo.

- **R4. Dockge ghi vào stack.** Dockge sửa compose trực tiếp qua web UI. Sau
  submodule, mỗi lần sửa trên UI sẽ làm repo con dirty — phải nhớ commit cả hai
  tầng, nếu không lần rebuild sau mất thay đổi.

- **R5. Data vẫn ngoài git.** `.gitignore` chặn `**/data/**`, `**/*_data/**`,
  `**/config/**`, `**/postgres/**`. Submodule không đổi điều đó: repo này quản
  CẤU HÌNH, không phải backup. Postgres của immich/n8n/dokploy, thư viện
  jellyfin, và mọi `.env` đều không có trong git.
