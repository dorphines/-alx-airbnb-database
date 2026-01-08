import datetime
from alx_backend_graphql_crm.schema import schema

def log_crm_heartbeat():
    timestamp = datetime.datetime.now().strftime('%d/%m/%Y-%H:%M:%S')
    message = f"{timestamp} CRM is alive\n" # Note: \n here is intentional for f-string formatting
    
    # Optional: verify graphql endpoint
    try:
        result = schema.execute("{ hello }")
        if not result.errors:
            message = f"{timestamp} CRM is alive and GraphQL is responsive\n"
    except Exception:
        pass

    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(message)

def update_low_stock():
    mutation = """
    mutation {
      updateLowStockProducts {
        success
        message
        updatedProducts {
          name
          stock
        }
      }
    }
    """
    result = schema.execute(mutation)
    if not result.errors:
        data = result.data['updateLowStockProducts']
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('/tmp/low_stock_updates_log.txt', 'a') as f:
            f.write(f"{timestamp} - {data['message']}\n")
            if data['updatedProducts']:
                for product in data['updatedProducts']:
                    f.write(f"  - {product['name']}: New stock {product['stock']}\n")
