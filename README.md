
#### Table of contents

1. [Overview](#docker-influxdb-grafana)
2. [disk_usage_cronjob repo structure](#disk_usage_cronjob-repo-structure)
3. [Grafana Disk Usage Dashboard](#grafana-disk-usage-dashboard)
4. [Run app by docker-compose](#run-app-by-docker-compose)
5. [kubectl deployments](#kubectl-deployments)

## Docker Influxdb Grafana

The main idea of this project is to create 3 docker containers (Influx, Grafana, disk_usage_cronjob)
And to record the disk usage in influxdb container and plot the disk usage graph in grafana so we can monitor the disk usage.


| Containers         | Entry URL                 |
| :----------------: | :------------------------:|
| Influx             | http://63.33.190.1:3000   |
| Grafana            | http://63.33.190.1:8086   |
| disk_usage_cronjob | -                         |


## disk_usage_cronjob repo structure:
```
- src/
   - utils/
        - __init__.py
        - config.py
        - disk_usage.py
        - influxdb_v2.py
   - main.py
```

## Grafana Disk Usage Dashboard:
![Disk-usage-dashboard](https://user-images.githubusercontent.com/32979588/144740078-6b38121e-254a-4dca-8f8d-6eaaa6acf7c3.PNG)

## Run app by docker-compose
```bash
$ docker-compose up --build
```

## Kubectl deployments
![image](https://user-images.githubusercontent.com/32979588/144723759-aaf266eb-2ef7-485b-bada-fad8409fb321.png)

