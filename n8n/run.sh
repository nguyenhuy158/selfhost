
ARCH=$(uname -m)
COMPOSE_FILE='./compose.yml'

PROJECT_DB='n8n_postgres'
DATABASE='n8n'
DUMP='./pgdump_n8n.sql'

function compose_cmd () {
    cmd="docker compose -f ${COMPOSE_FILE} $@"
    echo $cmd
    eval " $cmd"
}

# Main Flow
if [ -z "$1" ]
then
    compose_cmd up
fi
if [ $1 = "n8n" ]
then
    compose_cmd up -d
    exit 0
fi
if [ $1 = "restore" ]
then
    shift
    while [ "$1" != "" ]; do
        case $1 in
            --dump )       shift
                           DUMP="$1"
                           ;;
            *)             break
        esac
        shift
    done

    echo $DUMP
    # confirm

    compose_cmd down -v
    compose_cmd up -d postgres
    #wait for psql started
    for i in {1..10}; do
        docker logs ${PROJECT_DB} | grep -q 'database system is ready to accept connections'
        if [ $? -eq 0 ]; then
            break
        fi
        if [ $i -eq 7 ]; then
            echo "Postgres did not start up successfully"
            exit 1
        fi
        sleep 2
    done
    cmd="docker exec -i -e PGPASSWORD=n8n_password ${PROJECT_DB} psql -U n8n_user -d n8n -A < $DUMP"
    echo $cmd
    eval " $cmd"

    compose_cmd up -d n8n

else
    compose_cmd $@
    exit 0
fi
