FROM sergioestebanp/domoticpi:services-1.1
WORKDIR ./DomoticPi/DomoticPi_backend/device-service
ENTRYPOINT git -C /DomoticPi fetch && \
    git reset --hard origin/master && \
    python3 device-service.py
