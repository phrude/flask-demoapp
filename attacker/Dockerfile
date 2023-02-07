FROM python:3.10-alpine

WORKDIR /app

RUN pip install -U flask

COPY . .

CMD ["python", "-u", "main.py"]

