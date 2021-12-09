# set base image (host OS)
FROM python:3.8-slim-buster
# set the working directory in the container
WORKDIR /app
# install openssh & sshpass in the docker container
RUN apt-get update && apt-get install -y sshpass openssh-client
# generage ssh key with passphrase password
RUN ssh-keygen -t rsa -f /root/.ssh/id_rsa -P password
# change permissions of id_rsa
RUN chmod 500 /root/.ssh/id_rsa
# copy the dependencies file to the working directory
COPY requirements.txt .
# copy the environment variables
COPY .env.example .env
# install dependencies
RUN pip install -r requirements.txt
# copy the content of the local src directory to the working directory
COPY src/ .
# add execute permission wait-for-it.sh
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
# expose SSH port
EXPOSE 2222
# command to run on container start
CMD ["python", "main.py"]