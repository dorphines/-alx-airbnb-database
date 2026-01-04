# Documentation for `0-log_queries.py`

This document explains the `0-log_queries.py` script, which implements a Python decorator to log SQL queries before they are executed. This is a common pattern for enhancing observability and debugging in applications that interact with databases.

## The `log_queries` Decorator

The `log_queries` decorator is designed to wrap functions that execute SQL queries. Its primary purpose is to print the SQL query to `stderr` just before the wrapped function is called.

### How it Works

```python
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or args[0] if args else None
        if query:
            print(f"Executing query: {query}", file=sys.stderr)
        return func(*args, **kwargs)
    return wrapper
```

1.  **`log_queries(func)`**: This is the decorator function. It takes the function to be decorated (`func`) as an argument.

2.  **`@functools.wraps(func)`**: This is another decorator that helps preserve the metadata of the original function (`func`). This means that inspecting `fetch_all_users` (e.g., its name, docstring) after it's been decorated will show the original function's metadata, not the `wrapper`'s.

3.  **`wrapper(*args, **kwargs)`**: This is the inner function that will replace the original `func`. It accepts any arguments (`*args`, `**kwargs`) that the original function might take.

4.  **Extracting the Query**: Inside the `wrapper`, it attempts to extract the SQL query string. It first checks for a keyword argument named `query`. If not found, it checks if the first positional argument (`args[0]`) is the query. This makes the decorator flexible for functions where the query might be passed in different ways.

5.  **Logging**: If a `query` is found, it's printed to `sys.stderr` with a prefix "Executing query:". Logging to `stderr` is a common practice for diagnostic messages, separating them from the main program output.

6.  **Function Execution**: Finally, `func(*args, **kwargs)` is called, executing the original database operation. The result of the original function is then returned by the `wrapper`.

### Benefits

*   **Observability:** Provides a clear log of all executed SQL queries, which is invaluable for debugging and understanding application behavior.
*   **Decoupling:** Keeps logging logic separate from the core business logic of the query execution function, making the code cleaner and easier to maintain.
*   **Reusability:** The `log_queries` decorator can be easily applied to any function that executes SQL queries, promoting code reuse.
