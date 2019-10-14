to run in windows CMD: 
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run --port=3000

to run in windows PowerShell:
> $env:FLASK_APP = "flaskr"
> $env:FLASK_ENV = "development"
> flask run

to run in linux: 
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run