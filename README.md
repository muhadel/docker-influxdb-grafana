
#### Table of contents

1. [Overview](#docker-influxdb-grafana)
2. [disk_usage_cronjob repo structure](#disk_usage_cronjob-repo-structure)
3. [Migrate from influxdb v1 to v2](#migrate-from-influxdb-v1-to-v2)
4. [Grafana Disk Usage Dashboard](#grafana-disk-usage-dashboard)
5. [Run app by docker-compose](#run-app-by-docker-compose)
6. [Manage app by minikube](#manage-app-by-minikube)

## Docker Influxdb Grafana

The main idea of this project is to create 3 docker containers (Influx, Grafana, disk_usage_cronjob)
And to record the disk usage in influxdb container and plot the disk usage graph in grafana so we can monitor the disk usage.


| Containers         | Entry URL                            |
| :----------------: | :-----------------------------------:|
| Grafana            | http://63.33.190.1/                  |
| InfluxDB           | http://63.33.190.1/influxdb/health   |
| disk_usage_cronjob | -                                    |


## disk_usage_cronjob repo structure:
```
- src/
   - utils/
        - __init__.py
        - config.py
        - disk_usage.py
        - influxdb_v1.py
        - influxdb_v2.py
   - main.py
```

## Migrate from influxdb v1 to v2:
```
1- In influxdb-pod.yaml change "image: influxdb:1.8" to "image: influxdb:latest"
2- In influxdb-pod.yaml change "influxd" to "/bin/sh -c /entrypoint.sh" 
3- In main.py change "utils.influxdb_v1" to "utils.influxdb_v2"
```

## Grafana Disk Usage Dashboard:
![image](https://user-images.githubusercontent.com/32979588/146164380-10ddec86-a163-4566-8ecd-ce35bd5dced0.png)


## Run app by docker-compose
```bash
$ docker-compose up --build
```

## Manage app by minikube
```bash
# Create Kubernetes resources
$ sh k8s\create-resources.sh

# Delete Kubernetes resources
$ sh k8s\delete-resources.sh
```

