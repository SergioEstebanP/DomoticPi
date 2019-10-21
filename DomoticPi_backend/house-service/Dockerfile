FROM sergioestebanp/domoticpi:services-1.0
WORKDIR ./DomoticPi/DomoticPi_backend/house-service
ENTRYPOINT git -C /DomoticPi fetch && \
    git -C /DomoticPi checkout unique-db && \
    git -C /DomoticPi pull > aux && \ 
    python3 house-service.py 