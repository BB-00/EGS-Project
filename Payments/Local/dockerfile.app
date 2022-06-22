FROM python:3.8-alpine

WORKDIR /backend

COPY backend/requirements.txt /backend/requirements.txt

RUN apk update && apk add python3-dev gcc libc-dev mariadb-connector-c-dev libffi-dev

RUN pip install --no-cache -r requirements.txt

COPY backend/.secret/ /backend/.secret

COPY backend/apis/ /backend/apis

COPY backend/database/ /backend/database

COPY backend/schemas/ /backend/schemas

COPY backend/static/ /backend/static

COPY backend/templates/ /backend/templates

COPY backend/main.py /backend/

COPY delay.sh /backend/

CMD ["./delay.sh"]