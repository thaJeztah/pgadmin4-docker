FROM python:2-alpine

ENV PGADMIN_VERSION=1.3 \
    PYTHONDONTWRITEBYTECODE=1

RUN apk add --no-cache alpine-sdk postgresql-dev \
 && echo "https://ftp.postgresql.org/pub/pgadmin3/pgadmin4/v${PGADMIN_VERSION}/pip/pgadmin4-${PGADMIN_VERSION}-py2.py3-none-any.whl" > requirements.txt \
 && pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && apk del alpine-sdk \
 && addgroup -g 50 -S pgadmin \
 && adduser -D -S -h /pgadmin -s /sbin/nologin -u 1000 -G pgadmin pgadmin \
 && mkdir -p /pgadmin/config /pgadmin/storage; \
 chown -R 1000:50 /pgadmin

EXPOSE 5050

COPY LICENSE config_local.py /usr/local/lib/python2.7/site-packages/pgadmin4/

USER pgadmin:pgadmin
CMD [ "python", "./usr/local/lib/python2.7/site-packages/pgadmin4/pgAdmin4.py" ]
VOLUME /pgadmin/
