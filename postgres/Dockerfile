FROM postgres
COPY pg_trgm.sql /docker-entrypoint-initdb.d
RUN usermod -u 1103 postgres && groupmod -g 1103 postgres
USER postgres
