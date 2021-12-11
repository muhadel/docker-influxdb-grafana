
#### Table of contents

1. [Overview](#docker-influxdb-grafana)
2. [disk_usage_cronjob repo structure](#disk_usage_cronjob-repo-structure)
3. [Grafana Disk Usage Dashboard](#grafana-disk-usage-dashboard)
4. [Run app by docker-compose](#run-app-by-docker-compose)

## Docker Influxdb Grafana

The main idea of this project is to create 3 docker containers (Influx, Grafana, disk_usage_cronjob)
And to record the disk usage in influxdb container and plot the disk usage graph in grafana so we can monitor the disk usage.


| Containers         | Entry URL                 |
| :----------------: | :------------------------:|
| Grafana             | http://63.33.190.1:3000   |
| InfluxDB           | http://63.33.190.1:8086/health   |
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
![Disk-usage-dashboard-in-MB](https://user-images.githubusercontent.com/32979588/144740522-6cf08649-5e7d-40f1-b147-ef0d99016bfb.png)


## Run app by docker-compose
```bash
$ docker-compose up --build
```

