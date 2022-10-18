#RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
#  && tar xzvf docker-17.04.0-ce.tgz \
#  && mv docker/docker /usr/local/bin \
#  && rm -r docker docker-17.04.0-ce.tgz

FROM python:3.9-slim-buster

COPY . /Appium-Ecommerece-Python
WORKDIR /Appium-Ecommerece-Python

RUN pip3 install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v"]
CMD tail -f /dev/null