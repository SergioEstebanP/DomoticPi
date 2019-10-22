FROM sergioestebanp/domoticpi:db-services-1.0
ARG schema_path=./DomoticPi/DomoticPi_backend/database-service/schema.sql 
WORKDIR ./DomoticPi
RUN git fetch && \
    git reset --hard origin/master
WORKDIR /
RUN cp ${schema_path} ./docker-entrypoint-initdb.d && \ 
    bash -f entrypoint.sh