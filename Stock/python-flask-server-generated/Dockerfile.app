FROM python:3.8-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apk update && apk add python3-dev gcc libc-dev libffi-dev mariadb-connector-c-dev

RUN pip3 install --no-cache-dir -r requirements.txt

RUN apk add --no-cache bash

COPY . /usr/src/app

EXPOSE 8080


CMD ["./delay.sh"]