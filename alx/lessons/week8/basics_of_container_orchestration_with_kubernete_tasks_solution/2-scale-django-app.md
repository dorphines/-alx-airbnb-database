# Task 2: Scale the Django App Using Kubernetes

## Objective
Learn how to scale applications in Kubernetes.

## Solution
A bash script `kubctl-0x01` was created to scale the Django app deployment to 3 replicas, verify the pods, perform load testing with `wrk`, and monitor resource usage.

### `messaging_app/kubctl-0x01`
```bash
#!/bin/bash

echo "Scaling Django app deployment to 3 replicas..."
kubectl scale deployment/django-messaging-app --replicas=3

echo "Verifying multiple pods are running..."
kubectl get pods

echo "Getting the URL for the django-messaging-service..."
SERVICE_URL=$(minikube service django-messaging-service --url)
echo "Service URL: $SERVICE_URL"

# Perform load testing using wrk (assuming wrk is installed)
echo "Performing load testing with wrk..."
wrk -t4 -c10 -d30s "$SERVICE_URL"

echo "Monitoring resource usage with kubectl top..."
kubectl top pods
```