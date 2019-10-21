FROM sergioestebanp/domoticpi:services-1.0
WORKDIR ./DomoticPi/DomoticPi_backend/user-service
ENTRYPOINT git -C /DomoticPi fetch && \
    git -C /DomoticPi checkout origin unique-db && \
    git -C /DomoticPi pull origin unique-db > aux && \ 
    python3 user-service.py 