FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/src/app
WORKDIR  /usr/src/app
COPY . /usr/src/app/
# RUN mkdir /usr/src/app/django3byexample/static

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
