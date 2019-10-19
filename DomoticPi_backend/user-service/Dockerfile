FROM sergioestebanp/domoticpi:services-1.0
WORKDIR ./DomoticPi/DomoticPi_backend/user-service
ENTRYPOINT git -C /DomoticPi pull && python3 user-service.py