FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apk update && apk add python3-dev gcc libc-dev libffi-dev mariadb-connector-c-dev netcat-openbsd

RUN pip install --no-cache-dir -r requirements.txt

COPY .secret/ /app/.secret

COPY auth.py db.py main.py delay.sh /app/

# RUN chmod u+x delay.sh

CMD ["./delay.sh"]