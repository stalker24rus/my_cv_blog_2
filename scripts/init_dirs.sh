#!/bin/bash
# Create dirs for using with docker volumes
mkdir /var/lib/postgresql \
        /var/log/django \
        /var/log/gunicorn \
        /var/log/nginx \
        /usr/src/www \
        /usr/src/www/assets \
        /usr/src/www/media \
        /usr/src/www/static

echo "Dirs is created"

# Change group permissions
chown -R :1101 /var/log/nginx

chown -R :1102 /var/log/django \
        /var/log/gunicorn \
        /usr/src/www/assets \
        /usr/src/www/media \
        /usr/src/www/static

chown -R :1103 /var/lib/postgresql

echo "Owner group is changed"

# Add permissions for group
chmod -R 775 /var/lib/postgresql \
        /var/log/django \
        /var/log/gunicorn \
        /var/log/nginx \
        /usr/src/www/assets \
        /usr/src/www/media \
        /usr/src/www/static

echo "Permissions for file by group is changed"
