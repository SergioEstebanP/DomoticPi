FROM ubuntu:latest

RUN apt update
RUN apt install -y git python3 python3-venv

ARG git_repository=https://github.com/SergioEstebanP/DomoticPi.git
   
RUN git clone ${git_repository}
WORKDIR DomoticPi/DomoticPi_backend/device-service

RUN python3 -m venv venv 
RUN source venv/bin/activate
RUN pip install mysql-connector-python flask
RUN export FLASK_ENV=development
RUN export FLASK_APP=device-service.py
RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8

ENTRYPOINT flask run