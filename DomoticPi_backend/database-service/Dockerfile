FROM sergioestebanp/domoticpi:db-services-1.0
ARG schema_path=/DomoticPi/DomoticPi_backend/database-service/schema.sql 
RUN git -C /DomoticPi fetch && \
    git -C /DomoticPi reset --hard origin/master && \
    cp ${schema_path} ./docker-entrypoint-initdb.d && \ 
    bash -f entrypoint.sh