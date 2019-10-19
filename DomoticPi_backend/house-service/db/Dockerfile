FROM sergioestebanp/domoticpi:db-services-1.0
ARG schema_path=./DomoticPi/DomoticPi_backend/house-service/db/schema.sql 
WORKDIR ./DomoticPi
RUN git pull
WORKDIR /
RUN cp ${schema_path} ./docker-entrypoint-initdb.d && \ 
    bash -f entrypoint.sh