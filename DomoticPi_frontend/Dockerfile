FROM sergioestebanp/domoticpi:front-services-1.0
WORKDIR ./DomoticPi/DomoticPi_frontend/flaskr
ENTRYPOINT git -C /DomoticPi pull > aux && python3 __init__.py