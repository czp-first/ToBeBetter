FROM python:3.10.12-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
# RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
RUN pip install -r requirements.txt --no-deps --no-cache-dir

ARG ENVIRONMENT=dev
ARG PG_HOST
ARG PG_PORT
ARG PG_USER
ARG PG_PASSWORD
ARG PG_DB
ARG LOG_FILE

ENV ENVIRONMENT=${ENVIRONMENT} \
    PG_HOST=${PG_HOST} \
    PG_PORT=${PG_PORT} \
    PG_USER=${PG_USER} \
    PG_PASSWORD=${PG_PASSWORD} \
    PG_DB=${PG_DB} \
    LOG_FILE=${LOG_FILE}

COPY . ./

EXPOSE 80

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80", "--workers=5"]
