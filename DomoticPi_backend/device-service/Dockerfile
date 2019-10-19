FROM sergioestebanp/domoticpi:services-1.0
WORKDIR ./DomoticPi/DomoticPi_backend/device-service
ENTRYPOINT git -C /DomoticPi pull && python3 device-service.py
