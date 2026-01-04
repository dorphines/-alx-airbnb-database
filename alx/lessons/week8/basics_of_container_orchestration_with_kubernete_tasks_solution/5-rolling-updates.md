# Task 5: Applying rolling updates

## Objective
Update the application without downtime

## Solution
The `blue_deployment.yaml` was modified to use a new Docker image version (`v2.0`). A bash script `kubctl-0x03` was created to apply the updated deployment, monitor the rolling update, and test for downtime using `curl`.

### Modified `messaging_app/blue_deployment.yaml`
The `image` was updated to `django-messaging-app:v2.0`.

### `messaging_app/kubctl-0x03`
```bash
#!/bin/bash

# Apply the updated deployment to trigger a rolling update
echo "Applying updated blue deployment to trigger a rolling update..."
kubectl apply -f blue_deployment.yaml

# Monitor the rolling update status in the background
echo "Monitoring rollout status..."
kubectl rollout status deployment/django-messaging-app-blue &

# Continuously test the service endpoint to check for downtime.
# This requires the service to be accessible, for example via port-forwarding:
# kubectl port-forward service/django-messaging-service 8080:80
echo "Testing for downtime with curl on http://localhost:8080 (requires port-forwarding)..."

ROLLOUT_IN_PROGRESS=true
while [ "$ROLLOUT_IN_PROGRESS" = true ]; do
    # Check if the rollout is still in progress
    kubectl rollout status deployment/django-messaging-app-blue --watch=false > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        ROLLOUT_IN_PROGRESS=false
    fi

    # Make a request to the service
    RESPONSE_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8080)
    if [ "$RESPONSE_CODE" -eq 200 ]; then
        echo -n "." # Success
    else
        echo -n "X" # Failure
    fi
    sleep 1
done

echo "\nRolling update monitoring complete."

# Verify the final state of the pods
echo "Verifying pods after rolling update..."
kubectl get pods -l app=django-messaging-app,version=blue

echo "Script finished."
```
