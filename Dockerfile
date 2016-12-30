FROM python:2-alpine

ENV PGADMIN_VERSION=1.0 \
    PYTHONDONTWRITEBYTECODE=1

RUN apk add --no-cache alpine-sdk postgresql-dev \
 && echo "https://ftp.postgresql.org/pub/pgadmin3/pgadmin4/v${PGADMIN_VERSION}/pip/pgadmin4-${PGADMIN_VERSION}-py2-none-any.whl" > requirements.txt \
 && pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && apk del alpine-sdk

EXPOSE 80

COPY LICENSE config_local.py /usr/local/lib/python2.7/site-packages/pgadmin4/

CMD [ "python", "./usr/local/lib/python2.7/site-packages/pgadmin4/pgAdmin4.py" ]
