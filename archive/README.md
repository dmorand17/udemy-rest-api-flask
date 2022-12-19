Rest APIs with Flask Udemy Training

[Source code from Udemy course](https://github.com/tecladocode/python-refresher)

## Formatting code

```bash
python3 -m black .
```

## Local Testing

Run the following from the root section folder (e.g. `section6`)

1. Create a virtual environment (_if one doesn't exist already_)

```bash
mkvirtualenv udemy-rest-section6
```

2. Launch virtual environment

```bash
workon udemy-rest-section6
```

3. Init database _(if necessary)_

```bash
./bin/init-database [-i [users,items,all]]
```

4. Launch application

```bash
UDEMY_RESTAPI_CONFIG=conf/config.yaml python3 app/app.py
```

OR using server-debug script

```bash
./bin/server-debug
```

## Docker

Perform the following steps to build a `section`

1. Build Image
2. Run

### Build image

Run the following command from the root `section` folder (e.g. `section6`)

```bash
docker build --build-arg=PROJ_DIR=app -t udemy-rest-api:latest .
```

### Run

```bash
docker run -d \
  --label "udemy-rest-api" \
  --env-file=.env \
  -p 8888:8888 \
  -v $(pwd)/section6/logs:/app/logs \
  -v $(pwd)/section6/conf:/app/conf \
  -v $(pwd)/section6/data.db:/app/data.db \
  udemy-rest-api
```

### Debugging

#### Run image (local debugging)

```bash
docker run -d \
  --label "udemy-rest-api" \
  --env-file=.env \
  -p 5050:8080 \
  -v $(pwd)/section6/app:/app \
  -v $(pwd)/section6/logs:/app/logs \
  -v $(pwd)/section6/conf:/app/conf \
  -v $(pwd)/section6/data.db:/app/data.db \
  udemy-rest-api
```

#### Run image w/console access

```bash
docker run -it udemy-rest-api /bin/bash
```

### Cleanup

Kill running containers and remove unused images

```bash
docker container kill $(docker ps --filter "label=udemy-rest-api" -q)
docker image rm
docker system prune -f
```

## Configuration

Most project folders have a `conf/config.yaml` file. This can be used to configure the database, and whether or not to initialize the database

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
