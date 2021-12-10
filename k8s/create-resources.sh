#!/bin/bash
echo "Deleting Namespace..."
KUB_NAME_SPACE=app
kubectl delete all --all -n $KUB_NAME_SPACE
kubectl delete namespace $KUB_NAME_SPACE
echo "Creating New Namespace..."
kubectl create ns $KUB_NAME_SPACE
# Grafana
echo "Creating Grafana Resources..."
kubectl apply -f k8s/deployments/grafana-deployment.yaml
kubectl apply -f k8s/services/grafana-service.yaml
# Influxdb
echo "Creating Influxdb Resources..."
kubectl apply -f k8s/configmap/env-influxdb-configmap.yaml
kubectl apply -f k8s/deployments/influxdb-deployment.yaml
kubectl apply -f k8s/services/influxdb-service.yaml
echo "Creating disk_usage_cronjob Resources..."
kubectl apply -f k8s/deployments/disk_usage_cronjob-deployment.yaml
kubectl apply -f k8s/services/disk_usage_cronjob-service.yaml
# Ingress
echo "Creating Ingress service..."
kubectl apply -f k8s/ingress/ingress.yaml
