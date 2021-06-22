Rest APIs with Flask Udemy Training

[Source code from Udemy course](https://github.com/tecladocode/python-refresher)

## Docker
### Build image
```bash
docker build --build-arg=start_dir=app -t udemy-rest-api .
```

### Run image
```bash
docker run -e WS_PORT=8080 --env-file=.env -p 5050:8080 udemy-rest-api
```
### Run image (testing)
```bash
docker run -it udemy-rest-api /bin/bash
```
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
