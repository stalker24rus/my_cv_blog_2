FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /usr/src/app
WORKDIR  /usr/src/app
COPY . /usr/src/app/
COPY www/env/settings/system /etc/systemd/system
# RUN apt-get update && apt-get install -y systemd-analyze
RUN pip install -r requirements.txt
