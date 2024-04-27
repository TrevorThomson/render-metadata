#!/bin/bash -f

set +e

service=$1

timestamp=$(date +%s)
success=
error=
count=0

echo "Polling for Cassandra Cluster availability..."

until [[ $success || $error ]]; do
    success=$(docker compose logs --since $timestamp $service | grep "Cluster available")
    error=$(docker compose logs --since $timestamp $service | grep "ERROR")
    if [[ $success || $error ]]; then
        done=1
    elif [[ $count > 100 ]]; then
        error="Error: $(basename $0) timed out..."
    else
        sleep 10
    fi
done

if [[ $error ]]; then
    docker compose logs --since $timestamp $service
    exit 1
else
    echo $success
    exit 0
fi
