FROM ubuntu:latest

RUN apt update
RUN apt install -y git python3 python3-pip

ARG git_repository=https://github.com/SergioEstebanP/DomoticPi.git
   
RUN git clone ${git_repository}
WORKDIR DomoticPi/DomoticPi_backend/device-service

RUN pip3 install mysql-connector-python flask

ENTRYPOINT python device-service.py

EXPOSE 5000
