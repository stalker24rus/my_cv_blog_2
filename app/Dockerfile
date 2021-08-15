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

RUN useradd appuser
RUN usermod -u 1102 appuser && groupmod -g 1102 appuser
RUN chown -R appuser:appuser /usr/src/app
RUN chown -R appuser:appuser /usr/local/lib/python3.9


USER appuser
