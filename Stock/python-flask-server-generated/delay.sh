#!/bin/sh
sleep 30
>&2 echo "Service is up - executing command"

python3 -m swagger_server