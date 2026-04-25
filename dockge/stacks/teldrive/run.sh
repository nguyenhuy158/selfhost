touch storage.db
docker network create caddy
docker volume create caddy_data
docker compose -f teldrive.yml up -d
docker compose -f imgproxy.yml up -d
docker compose -f caddy.yml up -d

