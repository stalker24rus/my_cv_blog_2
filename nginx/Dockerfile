FROM nginx:stable 
#1.20.1

RUN mkdir -p /usr/src/www/media
RUN mkdir -p /usr/src/www/static
RUN mkdir -p /etc/nginx/ssl

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

## add permissions for nginx user
RUN chown -R nginx:nginx /var/cache/nginx /etc/nginx/
RUN chown -R nginx:nginx /usr/src/www/media && \
    chown -R nginx:nginx /usr/src/www/static && \
    chown -R nginx:nginx /var/log/nginx && \
    chown -R nginx:nginx /etc/nginx/conf.d
RUN touch /var/run/nginx.pid && \
        chown -R nginx:nginx /var/run/nginx.pid

USER nginx

CMD ["nginx", "-g", "daemon off;"]
