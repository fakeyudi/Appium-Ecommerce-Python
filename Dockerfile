FROM python:3.9-slim-buster

COPY . /Appium-Ecommerece-Python
WORKDIR /Appium-Ecommerece-Python

RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null