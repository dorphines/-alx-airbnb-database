# Task 3: Schedule a GraphQL Mutation for Product Stock Alerts

## Objective
Create a `django-crontab` job that runs every 12 hours, using a GraphQL mutation to automatically restock products with low inventory.

## 1. Define the GraphQL Mutation
File: `crm/schema.py`

Add the `UpdateLowStockProducts` mutation class and include it in the `Mutation` class.

```python
class UpdateLowStockProducts(graphene.Mutation):
    updated_products = graphene.List(ProductType)
    success = graphene.Boolean()
    message = graphene.String()

    @staticmethod
    def mutate(root, info):
        # Query products with stock < 10
        low_stock_products = Product.objects.filter(stock__lt=10)
        updated_list = []
        for product in low_stock_products:
            # Increment stock by 10
            product.stock += 10
            product.save()
            updated_list.append(product)
        
        return UpdateLowStockProducts(
            updated_products=updated_list,
            success=True,
            message=f"Successfully updated {len(updated_list)} products."
        )

class Mutation(graphene.ObjectType):
    ...  # noqa
    update_low_stock_products = UpdateLowStockProducts.Field()
```

## 2. Define the Cron Job Function
File: `crm/cron.py`

Add the `update_low_stock` function that executes the mutation.

```python
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
    # Execute the mutation via the schema
    result = schema.execute(mutation)
    
    if not result.errors:
        data = result.data['updateLowStockProducts']
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('/tmp/low_stock_updates_log.txt', 'a') as f:
            f.write(f"{timestamp} - {data['message']}\n")
            if data['updatedProducts']:
                for product in data['updatedProducts']:
                    f.write(f"  - {product['name']}: New stock {product['stock']}\n")
```

## 3. Configure the Cron Job
File: `alx_backend_graphql_crm/settings.py`

Update `CRONJOBS` to include the new task.

```python
CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.log_crm_heartbeat'),
    ('0 */12 * * *', 'crm.cron.update_low_stock'),
]
```

## Instructions to apply:
1. Update the system crontab:
   ```bash
   python manage.py crontab add
   ```

