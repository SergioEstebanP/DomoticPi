FROM mysql-services-full
ARG schema_path=./DomoticPi/DomoticPi_backend/user-service/db/schema.sql 
WORKDIR ./DomoticPi
RUN git pull
WORKDIR /
RUN cp ${schema_path} ./docker-entrypoint-initdb.d && \ 
    bash -f entrypoint.sh