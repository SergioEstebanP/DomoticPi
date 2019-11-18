## Local Development
---

In order to develop in local computer, and avoid costs of time uploading code and upgrading services version in the containers, I provide the configuration for the virtualenv and running the services in local computer. Follow the next steps: 

1. Create a python virtual environment in this directory. If you are using a windows machine just type the following command: 
> `python -m venv venv`.
2. Then actiuvate it with the following command (Power-Shell commands): 
> `.\venv\scripts\Activate.ps1`
3. Now you have to isntall the required packages in order to make the application run, just type the following command: 
> `pip install -r .\requirements.txt`
4. Then just runn the application: 
> `python \service-selected\script-to-execute.py`
5. The console should show some output like the following. Just click in the direction and you'll be accessible to the software. Ready to develop: 
```
 * Serving Flask app "__init__" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 217-842-666
 * Running on http://0.0.0.0:3001/ (Press CTRL+C to quit)
```

NOTES: the only container you must run under docker is database-service. This service uses a mysql already docker container in order to storage the data properly. To run this container just type the following command: 
> `docker run -p 3306:3306 --name device-service-db -e MYSQL_ROOT_PASSWORD=device-service -d --net=services-nw device-service-db`