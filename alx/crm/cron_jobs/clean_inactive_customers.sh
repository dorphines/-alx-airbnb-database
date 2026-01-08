#!/bin/bash

# Path to the project root
PROJECT_ROOT="/home/dorfin/alx"
LOG_FILE="/tmp/customer_cleanup_log.txt"

# Navigate to project root
cd $PROJECT_ROOT

# Run the cleanup command via manage.py shell
DELETED_COUNT=$(python3 manage.py shell <<PYEOF 2>/dev/null
from django.utils import timezone
from datetime import timedelta
from crm.models import Customer
one_year_ago = timezone.now() - timedelta(days=365)
inactive_customers = Customer.objects.exclude(orders__order_date__gte=one_year_ago)
count = inactive_customers.count()
inactive_customers.delete()
print(count)
PYEOF
)

# Extract only the last line which contains the count
DELETED_COUNT=$(echo "$DELETED_COUNT" | tail -n 1)

# Log the result with a timestamp
echo "$(date '+%Y-%m-%d %H:%M:%S') - Deleted $DELETED_COUNT customers" >> $LOG_FILE
