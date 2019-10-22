FROM sergioestebanp/domoticpi:services-1.1
WORKDIR ./DomoticPi/DomoticPi_backend/house-service
ENTRYPOINT git -C /DomoticPi fetch && \
    git reset --hard origin/master && \
    python3 house-service.py