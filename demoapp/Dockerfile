FROM python:3.10-alpine

WORKDIR /app

RUN apk add --no-cache git

COPY ./requirements.txt /app/requirements.txt
RUN pip install -U -r requirements.txt

COPY . .

CMD python -u main.py
