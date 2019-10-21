FROM sergioestebanp/domoticpi:services-1.0
WORKDIR ./DomoticPi/DomoticPi_backend/device-service
ENTRYPOINT git -C /DomoticPi checkout unique-db && \
    git -C /DomoticPi pull origin unique-db > aux && \ 
    python3 device-service.py 
