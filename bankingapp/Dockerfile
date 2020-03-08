FROM python:3.8-alpine

WORKDIR /home/bankingapp/.
COPY requirements.txt /home/bankingapp/requirements.txt

RUN apk update && apk add gcc python3-dev zlib-dev jpeg-dev musl-dev postgresql-dev
RUN pip install --no-cache-dir -r /home/bankingapp/requirements.txt
