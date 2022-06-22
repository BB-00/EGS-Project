#!/bin/sh

# until nc -w 1 -z db 3306; do
#   >&2 echo "Service is unavailable - sleeping"
#   sleep 1
# done
sleep 30
>&2 echo "Service is up - executing command"

uvicorn main:app --proxy-headers --host 0.0.0.0 --port 9090
