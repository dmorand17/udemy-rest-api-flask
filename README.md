Rest APIs with Flask Udemy Training

- [Source code from Udemy course](https://github.com/tecladocode/python-refresher)
- [Documentation](https://rest-apis-flask.teclado.com/)
- [Python Refresher](https://github.com/tecladocode/python-refresher)

## Setup

Create virtual environment

```bash
python -m venv .venv
```

## Build

```bash
docker build -t flask-api .
```

## Run

### PROD mode

```bash
docker run -dp 5000:5000 flask-smorest-api
```

### DEBUG mode

```bash
docker run -d -p 5000:5000 \
--label "flask-smorest-api" \
-w /app \
-v "$(pwd):/app" \
flask-smorest-api
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
