Rest APIs with Flask Udemy Training

[Source code from Udemy course](https://github.com/tecladocode/python-refresher)

## Formatting code
```bash
python3 -m black .
```

## Testing locally
```bash
UDEMY_RESTAPI_CONFIG=conf/config.yaml python3 app/app.py
```
## Docker
### Build image
```bash
docker build --build-arg=PROJ_DIR=app -t udemy-rest-api .
```
### Run
```bash
docker run -d \
  --env-file=.env \
  -p 5050:5050 \
  -v ~/personal/udemy-rest-api-flask/section6/logs:/app/logs \
  -v ~/personal/udemy-rest-api-flask/section6/conf:/app/conf \
  -v ~/personal/udemy-rest-api-flask/section6/data.db:/app/data.db \
  udemy-rest-api
```

### Debugging
#### Run image (local debugging)
```bash
docker run -d \
  -e WS_PORT=8080 \
  --env-file=.env \
  -p 5050:8080 \
  -v ~/personal/udemy-rest-api-flask/section6/app:/app \
  -v ~/personal/udemy-rest-api-flask/section6/logs:/app/logs \
  -v ~/personal/udemy-rest-api-flask/section6/conf:/app/conf \
  -v ~/personal/udemy-rest-api-flask/section6/data.db:/app/data.db \
  udemy-rest-api
```
#### Run image (console access)
```bash
docker run -it udemy-rest-api /bin/bash
```

### Cleanup
Kill running containers and remove unused images
```bash
docker container kill $(docker ps -q)
docker system prune -f
```

## Configuration
Most project folders have a `conf/config.yaml` file.  This can be used to configure the database, and whether or not to initialize the database
```
---
  database: data.db
  init_database: false
```

The database can be bootstrapped by running `python3 connection/db.py -i [all|users|items]`
##
## Rest-api-sections
[Section code](https://github.com/schoolofcode-me/rest-api-sections)

## Section 2 
[Sample Code](https://github.com/schoolofcode-me/rest-api-sections/tree/master/section2)

## Section 4
[Sample Code](https://github.com/schoolofcode-me/rest-api-sections/tree/master/section4)

## Section 5
[Sample Code](https://github.com/schoolofcode-me/rest-api-sections/tree/master/section5)

## Section 6
[Sample Code](https://github.com/schoolofcode-me/rest-api-sections/tree/master/section6)

## Section 7
[Sample Code](https://github.com/schoolofcode-me/rest-api-sections/tree/master/section7)

## Section 8
[Sample Code](https://github.com/schoolofcode-me/rest-api-sections/tree/master/section8)
