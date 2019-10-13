FROM ubuntu-services-full
WORKDIR ./DomoticPi/DomoticPi_backend/device-service
ENTRYPOINT git -C /DomoticPi pull && python3 device-service.py
