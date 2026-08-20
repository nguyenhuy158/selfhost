# Sinh dòng htpasswd cho basic auth của Traefik/nginx.
# `sed` nhân đôi dấu $ vì docker compose coi $ là ký tự nội suy biến.
#
# Cài: sudo apt install apache2-utils
# Dùng: ./gen.pass.sh <user> <password>
#
# Trước đây password thật nằm thẳng trong file này — đã gỡ, truyền qua tham số.

set -eu

USER="${1:?thieu tham so: user}"
PASS="${2:?thieu tham so: password}"

echo "$(htpasswd -nb "$USER" "$PASS")" | sed -e s/\\$/\\$\\$/g
