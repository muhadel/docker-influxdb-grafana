# set base image (host OS)
# FROM python:3.8-alpine
# FROM python:3.6-bullseye
FROM python:3.8-slim-buster
# FROM debian:11-slim
# create app user 
# RUN adduser -S appuser wheel
# # tell docker that all future commands should run as the appuser user
# USER appuser
# set the working directory in the container
WORKDIR /app

# install openssh in the docker container
# RUN apk add --no-cache openssh
# RUN apk add --update ; apk add --no-cache util-linux iproute2 net-tools iputils iperf tcptraceroute openssh openssh-server
RUN apt-get update && apt-get install -y openssh-server && apt-get install sshpass
RUN ssh-keygen -t rsa -f /root/.ssh/id_rsa -P password
# RUN sshpass -p influxdb ssh-copy-id -i /root/.ssh/id_rsa.pub -o StrictHostKeyChecking=no influxdb@influxdb

# copy the dependencies file to the working directory
COPY requirements.txt .
# copy the .env.example to .env
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