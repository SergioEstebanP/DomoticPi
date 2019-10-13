FROM ubuntu-services-full
WORKDIR ./DomoticPi/DomoticPi_backend/house-service
ENTRYPOINT git -C /DomoticPi pull && python3 house-service.py