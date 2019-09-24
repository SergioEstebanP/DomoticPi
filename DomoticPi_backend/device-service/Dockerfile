FROM ubuntu:latest

RUN apt update
RUN apt install -y git python

ARG git_repository=https://github.com/SergioEstebanP/DomoticPi.git
   
RUN git clone ${git_repository}
WORKDIR DomoticPi/DomoticPi_backend/device-service

RUN python -m venv venv 
RUN source venv/bin/activate
RUN pip install mysql-connector-python flask
