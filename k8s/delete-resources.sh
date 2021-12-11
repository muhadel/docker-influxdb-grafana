#!/bin/bash
KUB_NAME_SPACE=app
kubectl delete all --all -n $KUB_NAME_SPACE
kubectl delete namespace $KUB_NAME_SPACE

