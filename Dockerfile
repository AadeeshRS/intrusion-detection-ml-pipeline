FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN apt update && apt install awscli -y 
RUN apt-get update && pip install -r requirements.txt


CMD ["python", "app.py"]