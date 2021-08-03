FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/src/app
WORKDIR  /usr/src/app
COPY . /usr/src/app/

RUN mkdir -p /usr/src/www/static
RUN mkdir -p /usr/src/www/media
RUN mkdir -p /var/log/gunicorn

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
