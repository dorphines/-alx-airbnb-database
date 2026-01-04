# Task 4: Implement a Blue-Green Deployment Strategy

## Objective
Learn how to perform zero-downtime deployments.

## Solution
A blue-green deployment strategy was implemented by creating separate deployment files for the "blue" (current) and "green" (new) versions of the application. The original `deployment.yaml` was renamed to `blue_deployment.yaml`. A service file `kubeservice.yaml` was created to manage traffic switching, and a script `kubctl-0x02` was written to orchestrate the deployment process.

### `messaging_app/blue_deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: django-messaging-app-blue
spec:
  replicas: 1
  selector:
    matchLabels:
      app: django-messaging-app
      version: blue
  template:
    metadata:
      labels:
        app: django-messaging-app
        version: blue
    spec:
      containers:
      - name: django-messaging-app
        image: django-messaging-app:v2.0 # Using a versioned image
        imagePullPolicy: Never
        ports:
        - containerPort: 8000
```

### `messaging_app/green_deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: django-messaging-app-green
spec:
  replicas: 1
  selector:
    matchLabels:
      app: django-messaging-app
      version: green
  template:
    metadata:
      labels:
        app: django-messaging-app
        version: green
    spec:
      containers:
      - name: django-messaging-app
        image: django-messaging-app:v2.0 # New version of the image
        imagePullPolicy: Never
        ports:
        - containerPort: 8000
```

### `messaging_app/kubeservice.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: django-messaging-service
spec:
  selector:
    app: django-messaging-app
    # This selector will be updated to 'green' to switch traffic
    version: blue
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
  type: ClusterIP
```

### `messaging_app/kubctl-0x02`
```bash
#!/bin/bash

echo "Applying blue-green deployments and service..."

# Apply the service
kubectl apply -f kubeservice.yaml

# Apply the blue deployment
kubectl apply -f blue_deployment.yaml

# Apply the green deployment
kubectl apply -f green_deployment.yaml

echo "Waiting for green deployment to be available..."
kubectl rollout status deployment/django-messaging-app-green

echo "Checking logs for the green deployment..."
GREEN_PODS=$(kubectl get pods -l app=django-messaging-app,version=green -o jsonpath='{.items[*].metadata.name}')

for pod in $GREEN_PODS; do
    echo "Logs for pod: $pod"
    kubectl logs $pod
done

echo "Blue-green setup is complete. Traffic is currently on 'blue'."
echo "To switch traffic to 'green', update the selector in kubeservice.yaml to 'version: green' and run 'kubectl apply -f kubeservice.yaml'"
```
