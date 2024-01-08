#!/bin/bash

container_flags="--rm -it "

while [[ $# -gt 0 ]]; do
  case "$1" in
    --prod|-p )
      container_flags+=" -d"
      shift
      ;;
    * )
      echo "Usage: $0 [--prod]" 1>&2
      exit 1
      ;;
  esac
done

cd server
docker build -f docker/Dockerfile -t server --no-cache .        
if [[ $(docker volume ls | tail -n 1 | awk '{print $2}') != "sqlite-volume" ]]; then
    docker volume create sqlite-volume
fi 

docker run ${container_flags} -p 8000:8000 \
  -v sqlite-volume:$(pwd)/server \
    server
