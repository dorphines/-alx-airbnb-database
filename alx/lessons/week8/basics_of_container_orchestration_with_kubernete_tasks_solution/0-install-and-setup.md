# Task 0: Install Kubernetes and Set Up a Local Cluster

## Objective
Learn how to set up and use Kubernetes locally.

## Solution
A bash script `kurbeScript` was created to automate starting a local Kubernetes cluster using Minikube, verifying the cluster status, and listing the available pods.

### `messaging_app/kurbeScript`
```bash
#!/bin/bash

# Start a Kubernetes cluster using minikube
echo "Starting Kubernetes cluster..."
minikube start

# Verify that the cluster is running
echo "Verifying cluster status..."
kubectl cluster-info

# Retrieve available pods
echo "Retrieving available pods..."
kubectl get pods
```