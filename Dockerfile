FROM ubuntu:latest

# Reference - https://runnable.com/docker/python/dockerize-your-flask-application

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

ARG DB
ENV DB=${DB}

ARG PROJ_DIR
ENV PROJ_DIR=${PROJ_DIR}
RUN echo "Starting directory: $PROJ_DIR"

# We copy just the requirements.txt first to leverage Docker cache
COPY ${PROJ_DIR}/requirements.txt /app/requirements.txt
COPY ${DB} /app

WORKDIR /app
RUN pip3 install -r requirements.txt
COPY ${PROJ_DIR} /app

# Use ENTRYPOINT to lock down the image to python only 
# ENTRYPOINT ["/bin/echo","Hello"]
# CMD ["World"]

#ENTRYPOINT [ "python3" ]

CMD [ "python3", "app.py" ]
