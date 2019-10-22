FROM sergioestebanp/domoticpi:services-1.1
WORKDIR ./DomoticPi/DomoticPi_backend/user-service
ENTRYPOINT git -C /DomoticPi fetch && \
    git reset --hard origin/master && \
    python3 user-service.py