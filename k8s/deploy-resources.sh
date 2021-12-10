#!/bin/bash
pwd
KUB_NAME_SPACE=docker-influxdb-grafana
kubectl delete all --all -n $KUB_NAME_SPACE
kubectl delete namespace $KUB_NAME_SPACE
kubectl create ns $KUB_NAME_SPACE
kubectl apply -f k8s/deployments/grafana-deployment.yaml
kubectl apply -f k8s/services/grafana-service.yaml
kubectl apply -f k8s/ingress/ingress.yaml
