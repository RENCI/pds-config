FROM python:3.8-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip3 install --no-cache-dir flask gunicorn==20.0.4 connexion[swagger-ui] pymongo tx-functional>=0.1.2

COPY api /usr/src/app/api
COPY tx-utils/src /usr/src/app

EXPOSE 8080

ENTRYPOINT ["gunicorn"]

CMD ["-w", "4", "-b", "0.0.0.0:8080", "api.server:create_app()"]

