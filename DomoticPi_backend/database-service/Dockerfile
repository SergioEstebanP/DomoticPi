FROM sergioestebanp/domoticpi:db-services-1.0
ARG schema_path=./DomoticPi/DomoticPi_backend/database/schema.sql 
WORKDIR ./DomoticPi
RUN git fetch && \
    git checkout origin unique-db && \
    git pull origin unique-db
WORKDIR /
RUN cp ${schema_path} ./docker-entrypoint-initdb.d && \ 
    bash -f entrypoint.sh