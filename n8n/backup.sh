#!/bin/sh
pg='n8n_postgres'
docker exec -i $pg sh -c 'pg_dump -U n8n_user -d n8n' > "pgdump_n8n.sql"
