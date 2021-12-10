#!/bin/bash
KUB_NAME_SPACE=app
kubectl delete all --all -n $KUB_NAME_SPACE
kubectl delete namespace $KUB_NAME_SPACE
kubectl create ns $KUB_NAME_SPACE
# Grafana
kubectl apply -f k8s/deployments/grafana-deployment.yaml
kubectl apply -f k8s/services/grafana-service.yaml
# Influxdb
# kubectl apply -f k8s/deployments/influxdb-deployment.yaml
# kubectl apply -f k8s/services/influxdb-service.yaml
# Ingress
kubectl apply -f k8s/ingress/ingress.yaml
