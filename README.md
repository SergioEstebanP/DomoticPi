To do list: 
- Doc all the services
- Move db credentials to private file and add it to .gitignore
- Move credentials, directions and ip to external file
- Add requirement file for pip
- An improvement could be, instead of download the repository in the images, execute an script every time the docker containers start. In this way we can update the respositorio and jus restarting the container, the code is going to be updated and we dont have to stop and remove the container, neither recreate the image and deploy it. Just rerunning the container it's ok. 