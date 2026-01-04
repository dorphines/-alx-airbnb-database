# Documentation for Retry Database Queries Decorator

This document explains the `3-retry_on_failure.py` script, which implements a Python decorator to automatically retry database operations that fail due to transient errors.

## The `retry_on_failure` Decorator

The `retry_on_failure` decorator enhances the robustness of database interactions by automatically re-executing a function if it encounters an exception. This is particularly useful for dealing with transient issues like network glitches or temporary database unavailability.

### How it Works

```python
def retry_on_failure(retries=3, delay=1):
    """A decorator that retries a function a certain number of times if it raises an exception."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i + 1}/{retries} failed: {e}", file=sys.stderr)
                    if i < retries - 1:
                        time.sleep(delay)
            raise # Re-raise the last exception if all retries fail
        return wrapper
    return decorator
```

1.  **Outer Function `retry_on_failure(retries, delay)`**: This acts as a decorator factory. It allows you to configure the retry behavior (number of `retries` and `delay` between retries).

2.  **Inner Decorator `decorator(func)`**: This is the actual decorator that takes the function to be wrapped (`func`).

3.  **`wrapper(*args, **kwargs)`**: This inner function replaces the original `func`.

4.  **Retry Loop**:
    *   `for i in range(retries)`: The code attempts to execute the `func` a specified number of times.
    *   `try...except`: If the `func` executes successfully, its result is returned immediately. If an `Exception` occurs:
        *   An error message is printed to `stderr`.
        *   If there are retries left (`i < retries - 1`), the program waits for `delay` seconds using `time.sleep()`.
        *   If all retries fail, the last exception is re-raised, indicating a persistent failure.

### Parameters

*   **`retries` (default=3):** The maximum number of times to retry the function.
*   **`delay` (default=1):** The time in seconds to wait between retries.

### Integration with `with_db_connection`

The `retry_on_failure` decorator can be stacked with other decorators, such as `with_db_connection`, to provide comprehensive handling for database operations:

```python
@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    # ... database logic ...
```

### Benefits

*   **Resilience:** Makes database operations more robust against temporary failures.
*   **Automatic Handling:** Reduces the need for manual `try-except` blocks and retry logic in application code.
*   **Configurable:** The `retries` and `delay` parameters allow customization of the retry policy.
*   **Improved User Experience:** For transient errors, users might not even notice a temporary hiccup if the operation succeeds on a retry.
