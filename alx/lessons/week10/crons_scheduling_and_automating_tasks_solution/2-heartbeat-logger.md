# Task 2: Heartbeat Logger with django-crontab

## Objective
Implement a heartbeat logger using `django-crontab` that logs the application's health status every 5 minutes.

## 1. Update requirements.txt
Add `django-crontab` to the project requirements.

```text
django-crontab==0.7.1
```

## 2. Update settings.py
File: `alx_backend_graphql_crm/settings.py`

Add `django_crontab` to `INSTALLED_APPS` and define `CRONJOBS`.

```python
INSTALLED_APPS = [
    ...
    'django_filters',
    'django_crontab',
]

CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.log_crm_heartbeat'),
]
```

## 3. Define the Cron Job
File: `crm/cron.py`

```python
import datetime
from alx_backend_graphql_crm.schema import schema

def log_crm_heartbeat():
    timestamp = datetime.datetime.now().strftime('%d/%m/%Y-%H:%M:%S')
    message = f"{timestamp} CRM is alive\n"
    
    # Optionally verify GraphQL endpoint responsiveness
    try:
        result = schema.execute("{ hello }")
        if not result.errors:
            message = f"{timestamp} CRM is alive and GraphQL is responsive\n"
    except Exception:
        pass

    with open('/tmp/crm_heartbeat_log.txt', 'a') as f:
        f.write(message)
```

## Instructions to apply:
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Add cron jobs to the system:
   ```bash
   python manage.py crontab add
   ```
3. To view active cron jobs:
   ```bash
   python manage.py crontab show
   ```
