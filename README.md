Rest APIs with Flask Udemy Training

- [Source code from Udemy course](https://github.com/tecladocode/python-refresher)
- [Documentation](https://rest-apis-flask.teclado.com/)
- [Python Refresher](https://github.com/tecladocode/python-refresher)

## Setup

Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

## Build

```bash
docker build -t flask-api --build-arg PROJ_DIR=<directory> .
```

_Example_

```bash
docker build -t flask-api --build-arg PROJ_DIR=04-smorest-sqlalchemy .
```

## Run

### PROD mode

```bash
docker run -dp 5000:5000 flask-api
```

### DEBUG mode

```bash
# Change into project directory
cd 04-smorest-sqlalchemy

docker run -d -p 5000:5000 \
--label "flask-api" \
-w /app \
-v "$(pwd):/app" \
flask-api
```

**Tail logs**

```bash
docker logs -f $(docker ps -q --filter "label=flask-api")
```

## Formatting code

```bash
python3 -m black .
```

## Cleanup

Kill running containers and remove unused images

```bash
docker container kill $(docker ps --filter "label=flask-api" -q)
docker image rm
docker system prune -f
```
