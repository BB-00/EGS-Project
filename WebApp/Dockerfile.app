FROM python:3.8-alpine

WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt

RUN pip install -r requirements.txt

COPY . /backend

CMD ["python3", "run.py"]