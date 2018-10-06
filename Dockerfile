FROM ubuntu:latest

# Reference - https://runnable.com/docker/python/dockerize-your-flask-application
MAINTAINER Doug Morand "dmorand@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]