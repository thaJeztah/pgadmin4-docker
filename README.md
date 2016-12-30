# pgAdmin 4

This is a simple Docker image for running pgAdmin 4 in a container. It is not 
intended for production use (it runs in "desktop mode", so authentication
is disabled).

## Example use

```bash
# create a custom network for easier connecting
$ docker network create pg

# start a postgres container
$ docker run -d -e POSTGRES_PASSWORD=password --net pg --name postgres postgres

# start pgAdmin container
$ docker run -d -p 8080:80 --name pgadmin --net pg thajeztah/pgadmin4
```

Now visit `http://[your-docker-host]:8080` in your browser. You can add the
postgres database (password is `password`) to test if everything is working.

## Persistent data

Persistent data is stored in a volume, located at `/pgadmin/`. This allows
you to upgrade the container to a new version without losing configuration.

The following directories can be found inside the volume;

- `/pgadmin/config/pgadmin4.db` - SQLite configuration database
- `/pgadmin/storage/` - other storage

You can override the storage location by setting the `PG_ADMIN_DATA_DIR`
environment variable

## Run the image with a read-only filesystem

This image can be run with a read-only filesystem. To do so, specify the
`--read-only` flag when starting the container.

```bash
$ docker run -d -p 8080:80 --name pgadmin --read-only thajeztah/pgadmin4
```

## Runtime configuration

This image can be configured at runtime, by setting environment variables;

- `PG_ADMIN_DATA_DIR` directory to use for storing data (defaults to `/pgadmin/`)
- `PG_ADMIN_PORT` port to listen on (defaults to `80`)
- `DEBUG` enable debug mode (detaults to `False`)

More information on pgAdmin 4 development can be found here;

- https://git.postgresql.org/gitweb/?p=pgadmin4.git;a=summary
- https://www.pgadmin.org
