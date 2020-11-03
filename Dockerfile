FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk --no-cache add gcc musl-dev libffi-dev make
RUN pip3 install --no-cache-dir flask gunicorn[gevent]==19.9.0 connexion[swagger-ui] python-dateutil tx-functional==0.0.17 pint

COPY api /usr/src/app/api
COPY pdsphenotypemapping /usr/src/app/pdsphenotypemapping
COPY tx-utils/src /usr/src/app

ENTRYPOINT ["gunicorn"]

CMD ["-w", "4", "-b", "0.0.0.0:8080", "api.server:create_app()"]

