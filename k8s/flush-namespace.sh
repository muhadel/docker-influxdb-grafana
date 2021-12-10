#!/bin/bash
KUB_NAME_SPACE=myapp
kubectl delete all --all -n $KUB_NAME_SPACE
kubectl delete namespace $KUB_NAME_SPACE
kubectl create ns $KUB_NAME_SPACE
