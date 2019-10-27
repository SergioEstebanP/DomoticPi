FROM sergioestebanp/domoticpi:front-services-1.0
WORKDIR ./DomoticPi/DomoticPi_business_frontend/flaskr
ENTRYPOINT git -C /DomoticPi fetch && \
    git reset --hard origin/master && \
    python3 business-frontend.py