# Create the docker container for the backend
FROM balenalib/raspberrypi3-debian-python
WORKDIR /app
COPY App/requirements.txt /app
COPY App /app
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt \
