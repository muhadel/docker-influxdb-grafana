# set base image (host OS)
FROM python:3.8-slim-buster
# set the working directory in the container
WORKDIR /app
# install openssh & sshpass in the docker container
RUN apt-get update && apt-get install -y sshpass openssh-client netcat
# generage ssh key with passphrase password
RUN ssh-keygen -t rsa -f /root/.ssh/id_rsa -P ""
# change permissions of id_rsa
RUN chmod 600 /root/.ssh/id_rsa.pub
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
# add execute permission wait-for-it.sh
COPY wait-for.sh /wait-for.sh
RUN chmod +x /wait-for.sh
# command to run on container start
CMD ["python", "main.py"]