# Documentation for Reusable Query Context Manager

This document explains the `1-execute.py` script, which builds upon the previous task by creating a reusable, class-based context manager for executing SQL queries.

## The `ExecuteQuery` Context Manager

The `ExecuteQuery` class is a context manager that encapsulates the entire process of connecting to a database, executing a query, and fetching the results. This makes the code for running queries much cleaner and more reusable.

### The `__init__` Method
```python
def __init__(self, db_name, query, params=None):
    self.db_name = db_name
    self.query = query
    self.params = params if params is not None else ()
    self.results = None
```
*   The constructor takes the database name, the SQL query string, and an optional tuple of parameters for the query.

### The `__enter__` Method
```python
def __enter__(self):
    with DatabaseConnection(self.db_name) as cursor:
        cursor.execute(self.query, self.params)
        self.results = cursor.fetchall()
    return self.results
```
*   This method is where the magic happens.
*   It uses the `DatabaseConnection` context manager from the previous task to handle the database connection.
*   Inside the `with` block, it executes the query using the provided query string and parameters.
*   It fetches all the results and stores them in `self.results`.
*   Finally, it returns the results.

### The `__exit__` Method
```python
def __exit__(self, exc_type, exc_val, exc_tb):
    # No explicit cleanup needed here as DatabaseConnection handles it
    if exc_type:
        print(f"An exception occurred during query execution: {exc_val}")
    return False
```
*   In this case, the `__exit__` method doesn't need to do any cleanup because the `DatabaseConnection` context manager is already taking care of closing the connection.
*   It does, however, provide a place to handle any exceptions that might occur during the query execution.

## How it's Used

The main execution block of the script demonstrates how to use the `ExecuteQuery` context manager to run different queries.

```python
# Querying users older than 25
query_str = "SELECT * FROM users WHERE age > ?"
with ExecuteQuery(DB_NAME, query_str, (25,)) as users_over_25:
    for row in users_over_25:
        print(row)

# Querying all users
query_all_str = "SELECT * FROM users"
with ExecuteQuery(DB_NAME, query_all_str) as all_users:
    for row in all_users:
        print(row)
```

This approach makes the code much more readable and less repetitive. Instead of writing the connection and cursor logic every time we want to run a query, we can simply use the `ExecuteQuery` context manager.
