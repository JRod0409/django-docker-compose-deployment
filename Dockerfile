FROM python:3.9-alpine3.13
LABEL maintainer="henrybooks.com"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8000

# Install dependencies and build tools for Postgres/uWSGI
RUN apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev && \
    pip install --upgrade pip && \
    pip install -r /requirements.txt && \
    apk del .tmp-build-deps && \
    adduser -D -H appuser

USER appuser