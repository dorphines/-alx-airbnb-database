# Task 0: Schedule a Customer Cleanup Script

## Objective
Set up a shell script and a cron job to delete inactive customers (no orders in the last year) and log the results.

## 1. Create the Shell Script
File: `crm/cron_jobs/clean_inactive_customers.sh`

```bash
#!/bin/bash

# Path to the project root
PROJECT_ROOT="/home/dorfin/alx"
LOG_FILE="/tmp/customer_cleanup_log.txt"

# Navigate to project root
cd $PROJECT_ROOT

# Run the cleanup command via manage.py shell
DELETED_COUNT=$(python3 manage.py shell <<EOF 2>/dev/null
from django.utils import timezone
from datetime import timedelta
from crm.models import Customer
one_year_ago = timezone.now() - timedelta(days=365)
inactive_customers = Customer.objects.exclude(orders__order_date__gte=one_year_ago)
count = inactive_customers.count()
inactive_customers.delete()
print(count)
EOF
)

# Extract only the last line which contains the count
DELETED_COUNT=$(echo "$DELETED_COUNT" | tail -n 1)

# Log the result with a timestamp
echo "$(date '+%Y-%m-%d %H:%M:%S') - Deleted $DELETED_COUNT customers" >> $LOG_FILE
```

## 2. Create the Crontab Entry
File: `crm/cron_jobs/customer_cleanup_crontab.txt`

```text
0 2 * * 0 /bin/bash /home/dorfin/alx/crm/cron_jobs/clean_inactive_customers.sh
```

## Instructions to apply:
1. Ensure the script is executable:
   ```bash
   chmod +x crm/cron_jobs/clean_inactive_customers.sh
   ```
2. Add to crontab:
   ```bash
   crontab crm/cron_jobs/customer_cleanup_crontab.txt
   ```
