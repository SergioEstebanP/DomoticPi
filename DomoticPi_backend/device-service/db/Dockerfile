FROM mysql:latest

RUN apk update
RUN apk upgrade
RUN apk add git mysql

ARG git_repository=https://github.com/SergioEstebanP/DomoticPi.git
   
RUN git clone ${git_repository}
WORKDIR ./DomoticPi/DomoticPi_backend/device-service/db

# init database with own container command
RUN cp /docker-entrypoint-initdb.d .
RUN docker-entrypoint-initdb.d

EXPOSE 3306