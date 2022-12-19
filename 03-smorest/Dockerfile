FROM python:3.10
EXPOSE 5000
WORKDIR /app
# Import to have requirements installation prior to COPY . . to utilize caching
COPY requirements.txt .
# RUN pip install flask
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
