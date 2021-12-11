#!/bin/bash
echo "Deleting Namespace..."
KUB_NAME_SPACE=app
kubectl delete all --all -n $KUB_NAME_SPACE
kubectl delete namespace $KUB_NAME_SPACE
echo "Creating New Namespace..."
kubectl apply -f k8s/namespace/app-namespace.yaml
# Create Influxdb config maps
kubectl apply -f k8s/configmap/env-influxdb-configmap.yaml
# Grafana
echo "Creating Grafana Resources..."
# kubectl apply -f k8s/deployments/grafana-deployment.yaml
# kubectl apply -f k8s/services/grafana-service.yaml
# Influxdb
echo "Creating Influxdb Resources..."
# kubectl apply -f k8s/deployments/influxdb-deployment.yaml
kubectl apply -f k8s/pods/influxdb-pod.yaml
kubectl apply -f k8s/services/influxdb-service.yaml
echo "Creating cronjob config maps..."
echo "wait 4 seconds..."
sleep 4
INFLUXDB_POD_IP=$(kubectl exec influxdb-pod -n app -- hostname -I | xargs)
echo "INFLUXDB_POD_IP=$INFLUXDB_POD_IP"
cat k8s/configmap/env-cronjob-configmap.yaml | sed "s/{{INFLUXDB_POD_IP}}/$INFLUXDB_POD_IP/g" | kubectl apply -f -
echo "------------------------------------------------"
echo "Creating disk_usage_cronjob Resources..."
# kubectl apply -f k8s/deployments/cronjob-deployment.yaml
kubectl apply -f k8s/pods/cronjob-pod.yaml
kubectl apply -f k8s/services/cronjob-service.yaml
echo "------------------------------------------------"
# Ingress
echo "Creating Ingress service..."
kubectl apply -f k8s/ingress/ingress.yaml
