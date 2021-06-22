FROM ubuntu:latest

# Reference - https://runnable.com/docker/python/dockerize-your-flask-application

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

ARG start_dir
ENV start_dir=${start_dir}
RUN echo "Starting directory: $start_dir"

# We copy just the requirements.txt first to leverage Docker cache
COPY ${start_dir}/requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install -r requirements.txt
COPY ${start_dir} /app

# Use ENTRYPOINT to lock down the image to python only 
# ENTRYPOINT ["/bin/echo","Hello"]
# CMD ["World"]

#ENTRYPOINT [ "python3" ]

CMD [ "python3", "app.py" ]
