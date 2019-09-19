FROM alpine:latest

RUN apk update
RUN apk upgrade
RUN apk add git npm

ARG git_repository=https://github.com/SergioEstebanP/DomoticPi.git
   
RUN git clone ${git_repository}
WORKDIR DomoticPi/DomoticPi_backend/device-service

RUN npm install express
RUN npm install mysql

ENTRYPOINT node device-service.js &

EXPOSE 3000



