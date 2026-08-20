fswatch -or . | xargs -n1 sh -c 'echo "Restarting Docker..."; docker compose down && docker compose up -d'
