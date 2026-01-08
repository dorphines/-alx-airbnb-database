import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

URL = "http://localhost:8000/graphql"

transport = RequestsHTTPTransport(url=URL)
client = Client(transport=transport, fetch_schema_from_transport=True)

seven_days_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")

query = gql(
    f"""
    query {{
      allOrders(orderDate_Gte: "{seven_days_ago}") {{
        edges {{
          node {{
            id
            customer {{
              email
            }}
          }}
        }}
      }}
    }}
    """
)

LOG_FILE = "/tmp/order_reminders_log.txt"

try:
    response = client.execute(query)
    orders = response.get("allOrders", {}).get("edges", [])
    
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for edge in orders:
            node = edge["node"]
            order_id = node["id"]
            email = node["customer"]["email"]
            f.write(f"{timestamp} - Order ID: {order_id}, Customer Email: {email}\n")
    
    print("Order reminders processed!")
except Exception as e:
    print(f"Error: {e}")
