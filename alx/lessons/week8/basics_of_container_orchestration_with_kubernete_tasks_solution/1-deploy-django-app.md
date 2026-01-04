# Task 1: Deploy the Django Messaging App on Kubernetes

## Objective
Deploy your containerized Django app on Kubernetes.

## Solution
A `deployment.yaml` file was created to define the deployment and service for the Django messaging app. This file was later renamed to `blue_deployment.yaml` as part of Task 4. The initial deployment described a single instance of the application and a `ClusterIP` service to expose it internally.