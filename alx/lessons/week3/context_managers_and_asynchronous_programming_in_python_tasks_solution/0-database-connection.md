# Documentation for Custom Database Connection Context Manager

This document explains the `0-databaseconnection.py` script, which implements a custom, class-based context manager in Python to automatically handle database connections.

## The `DatabaseConnection` Context Manager

The core of the script is the `DatabaseConnection` class, which is designed to be used with Python's `with` statement. This ensures that the database connection is always closed properly, even if errors occur.

### The `__init__` Method
```python
def __init__(self, db_name):
    self.db_name = db_name
    self.conn = None
    self.cursor = None
```
*   The constructor takes the name of the database file as an argument.

### The `__enter__` Method
```python
def __enter__(self):
    self.conn = sqlite3.connect(self.db_name)
    self.cursor = self.conn.cursor()
    print(f"Database connection to {self.db_name} opened.")
    return self.cursor
```
*   This method is called when the `with` statement is entered.
*   It establishes a connection to the SQLite database and creates a cursor.
*   It returns the cursor object, which can then be used to execute queries.

### The `__exit__` Method
```python
def __exit__(self, exc_type, exc_val, exc_tb):
    if self.conn:
        self.conn.close()
        print(f"Database connection to {self.db_name} closed.")
    if exc_type:
        print(f"An exception occurred: {exc_val}")
    return False # Propagate exceptions
```
*   This method is called when the `with` block is exited.
*   It ensures that the database connection is closed.
*   The parameters `exc_type`, `exc_val`, and `exc_tb` are used to handle exceptions. If an exception occurred within the `with` block, these parameters will contain information about the exception.

## How it's Used

The script demonstrates how to use the `DatabaseConnection` context manager to set up a database and query it.

**1. Setting up the database:**
*   The `setup_database` function uses the context manager to create a `users` table and insert some sample data.

**2. Querying the database:**
*   The main execution block then uses the context manager again to connect to the database, execute a `SELECT` query, and print the results.

```python
with DatabaseConnection(DB_NAME) as cursor:
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for row in results:
        print(row)
```

By using the `with` statement, we can be sure that the database connection will be automatically closed when the block is finished, which is a much cleaner and safer way to manage resources than manually opening and closing the connection.
