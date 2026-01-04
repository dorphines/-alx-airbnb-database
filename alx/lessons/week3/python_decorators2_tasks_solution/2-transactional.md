# Documentation for Transaction Management Decorator

This document explains the `2-transactional.py` script, which implements a Python decorator for managing database transactions. This decorator ensures the atomicity of database operations, meaning that either all changes within a function are committed, or none are.

## The `transactional` Decorator

The `transactional` decorator is designed to wrap functions that perform one or more database write operations. It handles the `COMMIT` or `ROLLBACK` of a transaction based on whether the wrapped function executes successfully or raises an exception.

### How it Works

```python
def transactional(func):
    """A decorator that manages database transactions (commit/rollback)."""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()  # Commit if function executes successfully
            return result
        except Exception as e:
            conn.rollback() # Rollback if any exception occurs
            raise e
    return wrapper
```

1.  **`transactional(func)`**: This is the decorator function, taking the database operation function (`func`) as an argument.

2.  **`@functools.wraps(func)`**: Preserves the metadata of the original function.

3.  **`wrapper(conn, *args, **kwargs)`**: The inner function. It expects the database connection object (`conn`) as its first argument, as this is typically provided by the `with_db_connection` decorator.

4.  **Transaction Logic**:
    *   **`try...except` block**: This block encapsulates the execution of the original function.
    *   **`result = func(conn, *args, **kwargs)`**: The wrapped function is executed.
    *   **`conn.commit()`**: If `func` executes without raising an exception, the changes made to the database within that function are permanently saved.
    *   **`conn.rollback()`**: If `func` raises an exception, all changes made since the beginning of the transaction are undone, ensuring data integrity.
    *   **`raise e`**: After rolling back, the exception is re-raised so that calling code can handle it.

### Integration with `with_db_connection`

This script also includes the `with_db_connection` decorator from the previous task, which handles opening and closing the database connection. The `transactional` decorator is designed to work seamlessly with `with_db_connection`, as shown in the example:

```python
@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
```

This stacking of decorators provides a powerful and clean way to manage both connection handling and transaction management.

### Benefits

*   **Data Integrity:** Guarantees that database operations are atomic, preventing partial updates and inconsistent data.
*   **Simplified Error Handling:** Developers don't need to manually write `try...except` blocks with `commit` and `rollback` for every transactional operation.
*   **Code Reusability:** The `transactional` logic is encapsulated and can be applied to any function that requires transaction management.
*   **Readability:** Makes the code more declarative and easier to understand, as the intent of transaction management is explicitly stated with a decorator.
