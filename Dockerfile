FROM ubuntu:22.04

COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN apt-get update && \
    apt-get install -y python3 python3-venv && \
    python3 -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # apk add --update --no-cache --virtual .tmp-build-deps \
    #     iputils curl && \
    /py/bin/pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -rf /tmp
    # apk del .tmp-build-deps

ENV PATH="/py/bin:$PATH"

