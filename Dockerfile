# Should update this to use python:3 instead
FROM python:3.10-slim-buster

# Reference - https://runnable.com/docker/python/dockerize-your-flask-application

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

ARG PROJ_DIR
ENV PROJ_DIR=${PROJ_DIR}
RUN echo "Starting directory: $PROJ_DIR"

WORKDIR /app
# We copy just the requirements.txt first to leverage Docker cache
COPY ${PROJ_DIR}/requirements.txt .

RUN pip3 install -r requirements.txt
COPY ${PROJ_DIR} .

# Use ENTRYPOINT to lock down the image to python only 
# ENTRYPOINT ["/bin/echo","Hello"]
# CMD ["World"]

EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
