FROM sergioestebanp/domoticpi:front-services-1.0
WORKDIR ./DomoticPi/DomoticPi_frontend/flaskr
ENTRYPOINT git -C /DomoticPi fetch > aux && \
    git -C /DomoticPi unique-dbpython3 __init__.py