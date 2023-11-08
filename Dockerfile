FROM ubuntu:22.04

COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN apt-get update && \
    apt-get install -y python3 python3-venv iputils-ping -y curl && \
    python3 -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # apk add --update --no-cache --virtual .tmp-build-deps \
    #     iputils curl && \
    /py/bin/pip install --no-cache-dir -r /tmp/requirements.txt && \
    /py/bin/playwright install && \
    /py/bin/playwright install-deps
    # /py/bin/pip install libglib2.0-0 libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdbus-1-3 libdrm2 libxcb1 libxkbcommon0 libatspi2.0-0 libx11-6 libxcomposite1 libxdamage1 libxext6 libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 libasound2
  
    # rm -rf /tmp
    # apk del .tmp-build-deps

ENV PATH="/py/bin:$PATH"

