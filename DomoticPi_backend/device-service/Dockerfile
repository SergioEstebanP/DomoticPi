FROM ubuntu:latest

RUN apt update && \
    apt install -y git python3 python3-pip && \
ARG git_repository=https://github.com/SergioEstebanP/DomoticPi.git
RUN pip3 install mysql-connector-python flask

ENTRYPOINT git clone ${git_repository} && bash -f ./DomoticPi/DomoticPi_backend/device-service/init.sh