#!/bin/sh

sleep 30
>&2 echo "Service is up - executing command"

uvicorn main:app --proxy-headers --host 0.0.0.0 --port 9000