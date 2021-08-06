FROM nginx:1.20.1

RUN mkdir -p /usr/src/www/media
RUN mkdir -p /usr/src/www/static
RUN mkdir -p /etc/nginx/ssl

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
