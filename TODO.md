# TODO — selfhost

Rà soát ngày 2026-08-09. Đánh dấu `[x]` khi đã sửa VÀ đã verify chạy thật.

Việc gỡ 16 stack repo-lồng nằm riêng ở `PLAN-submodules.md` (S1–S10), không lặp
lại ở đây.

## A. Bảo mật — làm trước

- [ ] **A1. Rotate secret đã lộ.** Commit `d03b52d` gỡ secret khỏi compose sang
      `.env`, nhưng chúng đã nằm trong lịch sử git và đã push public. Gỡ khỏi
      file KHÔNG xoá được lịch sử — phải rotate ở nhà cung cấp:

      - Cloudflare Tunnel token (`cloudflared`) — quan trọng nhất, token này
        không hết hạn và dựng được đường vào mạng nội bộ. Zero Trust →
        Networks → Tunnels → chọn tunnel → rotate.
      - `cronmaster` AUTH_PASSWORD — đang là "huy". Container chạy
        `privileged: true` + `user: root`, mount docker.sock, sửa được crontab
        của root, lại publish ra cron.huyab.click. Ai vào được UI là chiếm host.
      - Netdata claim token (`netdata` và `ansible/ansible` dùng chung)
      - `beszel` agent token, `checkcle` SERVER_TOKEN
      - `homarr` SECRET_ENCRYPTION_KEY — CẢNH BÁO: đổi khoá này là mất sạch
        data đã mã hoá trong `./homarr/appdata`, cân nhắc trước.
      - `open-webui` WEBUI_SECRET_KEY — đổi thì mọi người bị đăng xuất, data giữ.

- [ ] **A2. `dozzle/data/users.yml` đang được git track.** `.gitignore` mới
      chặn `**/data/**` nhưng file đã track thì ignore không có tác dụng — mỗi
      commit vẫn mang theo bcrypt hash. Hash không đảo ngược được, nhưng để
      trên repo public là mời brute-force offline.
      → `git rm --cached dockge/stacks/dozzle/data/users.yml`

- [ ] **A3. Password mặc định của upstream còn nguyên.** Không phải leak (chúng
      public sẵn ở upstream) nhưng yếu thật, đang chạy thật:
      `photoprism` "insecure", `wordpress` root/wordpress, `pgadmin4` admin,
      `log` (grafana) admin, `nats` T0pS3cr3t, `minio`/`miniov2` adminadminadmin,
      `neko` neko/admin, `metabase` metabase_pass, `ai-scraper` huy/huy,
      `canine` password. Đổi giá trị mới là việc thật, không phải đưa vào .env.

## B. Đang lỗi

- [ ] **B1. `immich_power_tools` unhealthy.** App CHẠY BÌNH THƯỜNG
      (`✓ Ready in 2.2s`, Next.js 14.2.5) — chỉ healthcheck sai:

        wget: can't connect to remote host: Connection refused
        Connecting to localhost:3000 ([::1]:3000)

      `localhost` resolve ra IPv6 `::1` còn app chỉ listen IPv4. Sửa: đổi
      healthcheck sang `127.0.0.1:3000` thay vì `localhost:3000`.
      (Cùng loại với healthcheck `dockflare` đã sửa ở `d1a181d`.)

- [ ] **B2. `teldrive` chỉ còn `postgres_db` chạy**, app chính không lên. Xem
      là dừng dở hay compose hỏng.

## C. Dọn dẹp

- [ ] **C1. Hai container dockflare tự lên.** Lệnh `docker compose up -d` lúc
      sửa healthcheck đã khởi động `dockflare-picoshare-1` và
      `dockflare-internal-tool-1` — trước đó chúng đang tắt. Quyết: giữ hay tắt
      lại. Nếu không dùng thì bỏ khỏi compose, đừng để tắt/bật theo may rủi.

- [ ] **C2. Stack trùng nhau.** Mỗi cặp dùng chung `container_name` nên không
      chạy đồng thời được — giữ một, xoá một:

      | Cặp | Ghi chú |
      |-----|---------|
      | `server-control` vs `nguyenhuy158servercontrol` | cùng app `serverui`, CẢ HAI đang chạy |
      | `minio` vs `miniov2` | trùng cả credential lẫn container_name |
      | `netdata` vs `ansible/ansible` | trùng token, trùng container_name |

- [ ] **C3. 111/130 stack không chạy.** Rà xem cái nào bỏ hẳn được để repo khỏi
      phình. `superset` 294M, `firecrawl/repo` 134M, `syncthing` 977M,
      `sign0z` 84M — giờ là submodule nên không nặng repo cha, nhưng vẫn chiếm
      đĩa.

- [ ] **C4. `cloudflared-agent-dockflare-tunnel` không thuộc compose nào.**
      Dockflare tự sinh lúc runtime, không file nào trong repo mô tả nó. Mất là
      phải để dockflare tạo lại — chấp nhận được, nhưng cần biết.

## D. Giới hạn cần nhớ

Repo này quản **CẤU HÌNH**, không phải backup. `.gitignore` chặn
`**/data/**`, `**/*_data/**`, `**/config/**`, `**/postgres/**` và mọi `.env`.
Postgres của immich/n8n/dokploy, thư viện jellyfin, toàn bộ secret — không có
trong git. Máy chết thì repo dựng lại được cấu hình, KHÔNG dựng lại được dữ
liệu. Backup dữ liệu là việc riêng, chưa có.
