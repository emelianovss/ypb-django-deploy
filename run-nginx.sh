#!/bin/bash

mkdir -p static
mkdir -p media
docker run --rm \
  -v $PWD/static/:/var/www/static \
  -v $PWD/media/:/var/www/media \
  -v $PWD/default.conf:/etc/nginx/conf.d/default.conf:ro \
  --network=host \
  nginx
