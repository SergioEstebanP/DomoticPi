FROM ubuntu-services-full

WORKDIR ./DomoticPi
RUN git pull

WORKDIR ./DomoticPi_backend/user-service

ENTRYPOINT python3 user-service.py