FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/src/app
WORKDIR  /usr/src/app
COPY . /usr/src/app/

RUN mkdir -p /usr/src/www/static
RUN mkdir -p /usr/src/www/media
RUN mkdir -p /var/log/gunicorn
RUN mkdir -p /var/log/django

RUN mkdir -p /usr/src/config/gunicorn
COPY ./config/gunicorn /usr/src/config/gunicorn

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN useradd appuser && chown -R appuser /usr/src/app
USER appuser
