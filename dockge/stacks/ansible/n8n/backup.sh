#!/bin/sh
path="./"
pg='n8n_postgres'
cdate="$(date +"%y-%m-%d-%H-%M")"
while [ "$1" != "" ]; do
    case $1 in
        -p | --path )           shift
                                path=$1
                                ;;
        -n | --name )           shift
                                name=$1
                                ;;
        *) break
    esac
    shift
done

echo 'Docker container prefix: ' $name
echo 'Backup database to :' $path

# docker exec -i $pg sh -c 'pg_dump -U n8n_user -d n8n' > $path"pgdump_n8n_$cdate.sql"
docker exec -i $pg sh -c 'pg_dump -U n8n_user -d n8n' > $path"pgdump_n8n.sql"