FROM python:3.13-alpine

WORKDIR /flix-api

COPY . .

RUN apk add --no-cache \
    gcc \
    g++ \
    make \
    libc-dev \
    libpq-dev \
    pcre-dev \
    linux-headers

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod -R +x /flix-api/scripts

EXPOSE 8000

ENTRYPOINT ["/bin/sh", "/flix-api/scripts/entrypoint.sh"]