# Task 3: Set Up Kubernetes Ingress for External Access

## Objective
Expose your Django app to the internet using an Ingress controller.

## Solution
An `ingress.yaml` file was created to define an Ingress resource that routes traffic from `/api/` to the Django app's service. A `commands.txt` file was also created to store the command for applying the Ingress configuration.

### `messaging_app/ingress.yaml`
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: django-app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - http:
      paths:
      - path: /api/
        pathType: Prefix
        backend:
          service:
            name: django-app-service
            port:
              number: 80
```

### `messaging_app/commands.txt`
```
kubectl apply -f ingress.yaml
```
