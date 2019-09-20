FROM mysql:latest

ARG git_repository=https://github.com/SergioEstebanP/DomoticPi.git
ARG schema_path=./DomoticPi/DomoticPi_backend/device-service/db/schema.sql 

RUN apt -y update && \
    apt -y upgrade && \
    apt -y install git && \
    git clone ${git_repository} && \
    cp ${schema_path} ./docker-entrypoint-initdb.d && \ 
    bash -f entrypoint.sh