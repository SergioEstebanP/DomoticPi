## CI/CD for project
---

In this folder you can find all the files which manually aumates the deployment. We have a jenkins server who sends commands to a python server listening  for new deployments. 

In the future this tools should be replaced for some automatic ones like Ansible. I'm already working with a POC in ansible in order to auomate the deployment, but it's taking some time to fix the new errors. 

Interesting files: 

- `docker-compose.yml`: this file automate all the deployment. Just typing docker-compose up you can deploy all th services using docker without having to install nothing in your local computer. 
- `deploy.ps1`: Power-Shell script which activates docker-compose in order to launch the services. 
- `CICDServer.java`: java server who listen in a controled port, triggering new deployments for the services. 