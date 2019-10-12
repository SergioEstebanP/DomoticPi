FROM ubuntu-updated

ARG git_repository=https://github.com/SergioEstebanP/DomoticPi.git
RUN git clone ${git_repository} 

WORKDIR ./DomoticPi/DomoticPi_backend/house-service

RUN pip3 install mysql-connector-python flask

ENTRYPOINT python3 house-service.py