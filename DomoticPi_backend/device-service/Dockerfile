FROM sergioestebanp/domoticpi:services-1.0
WORKDIR ./DomoticPi/DomoticPi_backend/device-service
ENTRYPOINT git -C /domoticPi fetch &&\
    git -C /DomoticPi checkout unique-db && \
    git -C /DomoticPi pull > aux && \ 
    python3 device-service.py 
