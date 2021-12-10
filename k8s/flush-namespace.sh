#!/bin/bash
KUB_NAME_SPACE=docker-influxdb-grafana
kubectl delete all --all -n $KUB_NAME_SPACE
kubectl delete namespace $KUB_NAME_SPACE