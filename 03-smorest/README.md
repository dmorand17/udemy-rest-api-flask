# build project

```bash
docker build -t flask-smorest-api .
```

# run project

## PROD mode

```bash
docker run -dp 5000:5000 flask-smorest-api
```

## DEBUG mode

```bash
docker run -dp 5000:5000 \
-w /app \
-v "$(pwd):/app" \
flask-smorest-api
```

# SWagger

UI can be accessed at -> http://localhost:5000/swagger-ui
