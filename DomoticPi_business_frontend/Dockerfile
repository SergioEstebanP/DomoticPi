FROM sergioestebanp/domoticpi:services-1.0
WORKDIR ./DomoticPi/DomoticPi_business_frontend/flaskr
ENTRYPOINT git -C /DomoticPi pull > aux && python3 business-frontend.py