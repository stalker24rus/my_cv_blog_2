#!/bin/bash
# version 0.1

# Path for creating Nginx files and dir
NGINX_CONF_FILE='nginx/nginx.conf'
NGINX_DEFAULT_SSL_PATH='/etc/nginx/ssl'

# File template for NGINX SSL config 
ssl="
upstream my_cv_blog {
    server web:8000;
}

server {
    listen 443 default ssl;

    ssl_certificate /etc/nginx/ssl/$2.crt;
    ssl_certificate_key /etc/nginx/ssl/$2.key;
    
    ssl_protocols TLSv1.1 TLSv1.2;
    ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';
    ssl_prefer_server_ciphers on;
    ssl_session_cache shared:SSL:5m;
    # ssl_stapling on;
    # ssl_stapling_verify on;
    
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;
    
    location / {
        proxy_pass http://my_cv_blog;
       	proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header Host \$host;
        proxy_redirect off;
    }

    location /static/ {
        alias /usr/src/www/static/;
       	}

    location /media/ {
	alias /usr/src/www/media/;
        }
}

server {
     listen 80 default_server;
     server_name _;
     return 301 https://\$host\$request_uri;
}"


# File template for NGINX No SSL config 
nossl="
upstream my_cv_blog {
    server web:8000;
}

server {
    listen 80 default_server;
        
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;    
    location / {
        proxy_pass http://my_cv_blog;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	proxy_set_header Host $host;
        proxy_redirect off;
    }  
					        
    location /static/ {
        alias /usr/src/www/static/;
    }

    location /media/ {
	alias /usr/src/www/media/;
    }
}"

if [ "$1" = "--ssl" ]
then
	mkdir -p $NGINX_DEFAULT_SSL_PATH && chown -R :1101 $NGINX_DEFAULT_SSL_PATH && chmod -R 775 $NGINX_DEFAULT_SSL_PATH && echo "Created /etc/nginx/ssl"
	echo "${ssl}" > $NGINX_CONF_FILE && echo "Created a nginx.conf file for $2 sertificate with text:" && cat $NGINX_CONF_FILE
elif [ "$1" = "--nossl" ]
then 
	echo "${nossl}" > $NGINX_CONF_FILE  && echo "Created a nginx.conf file with text:" && cat $NGINX_CONF_FILE
else
	echo "Wrong argument! "
fi

