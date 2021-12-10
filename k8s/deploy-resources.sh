#!/bin/bash
pwd
kubectl apply -f ./deployments/grafana-deployment.yaml
kubectl apply -f ./services/grafana-service.yaml
kubectl apply -f ./ingress/ingress.yaml
