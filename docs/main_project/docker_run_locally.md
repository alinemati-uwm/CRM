# Run the project in Docker local mode

## For the first time, if you want to run the project in widnows without database and other services, you can run:

```bash
# this will remove all volumes and containers
docker compose -f docker/development/docker-compose.yml down -v
```

## this will remove all volumes and containers

```bash
docker compose -f docker/development/docker-compose.yml down --volumes --rmi all
```

```bash
# docker builder prune -f
```

for .env will build the project with development environment variables:

```bash
docker compose --env-file .env -f docker/development/docker-compose.yml up --build -d
```

add no-cache to build without cache:

```bash
docker compose --env-file .env -f docker/development/docker-compose.yml build --no-cache
```

## add user to project:

.env with run makemigrations:

```bash
docker compose --env-file .env -f docker/development/docker-compose.yml run --rm crm_web sh -c "python manage.py makemigrations"
```

here .env with run migrate:

```bash
# .env
docker compose --env-file .env -f docker/development/docker-compose.yml run --rm crm_web sh -c "python manage.py migrate"
```

How to create a superuser admin in docker:

.env with run createsuperuser:

```bash
docker compose --env-file .env -f docker/development/docker-compose.yml run --rm crm_web sh -c "python manage.py createsuperuser"
```

How to log into the project:

.env with run logs:

```bash
docker compose  --env-file .env -f docker/development/docker-compose.yml logs -f crm_web
```

shell to run commands in the project:

.env with run shell:

```bash
docker compose --env-file .env -f docker/development/docker-compose.yml run --rm crm_web sh -c "python manage.py shell"
```

collectstatic the project:

.env with run collectstatic:

```bash
docker compose --env-file .env -f docker/development/docker-compose.yml run --rm crm_web sh -c "python manage.py collectstatic"
```

Check the project for any issues:

.env with run check:

```bash
docker compose --env-file .env -f docker/development/docker-compose.yml run --rm crm_web sh -c "python manage.py check"
```

###############################################

# Run tests

###############################################

Run the tests in the project:

.env with run test:

```bash
docker compose --env-file .env -f docker/development/docker-compose.yml run --rm crm_web sh -c "python manage.py test"

docker compose --env-file .env -f docker/development/docker-compose.yml run --rm crm_web sh -c "sleep 5 && python manage.py test"

docker compose --env-file .env -f docker/development/docker-compose.yml run --rm crm_web  sh -c "pytest --reuse-db --tb=short -v tests/integration_test"

```

docker compose --env-file .env.local -f docker/development/docker-compose.yml run --rm crm_web sh -c "sleep 5 && python manage.py test"
docker compose --env-file .env.local -f docker/development/docker-compose.yml run --rm crm_web sh -c "pytest --reuse-db --tb=short -v tests/integration_test"

###############################################

# Run server

###############################################
Run server

.env with run server:

```bash
docker compose -f docker/development/docker-compose.yml run --rm crm_web sh -c "python manage.py runserver 0.0.0.0:8000"
```
