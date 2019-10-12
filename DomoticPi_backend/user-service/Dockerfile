FROM ubuntu-services

ARG git_repository=https://github.com/SergioEstebanP/DomoticPi.git
RUN git clone ${git_repository} 

WORKDIR ./DomoticPi/DomoticPi_backend/user-service

ENTRYPOINT python3 user-service.py