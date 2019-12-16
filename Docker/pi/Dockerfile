# Create the docker container for the backend
FROM python:3.7.3-alpine3.9
WORKDIR /app
COPY App/requirements.txt /app
COPY App /app
RUN apk update \
  && apk add --virtual build-deps gcc python-dev musl-dev \
  && pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt \