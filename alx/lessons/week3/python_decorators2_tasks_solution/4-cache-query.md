# Documentation for Cache Database Queries Decorator

This document explains the `4-cache_query.py` script, which implements a Python decorator to cache the results of database queries. This technique is crucial for optimizing performance by avoiding redundant and potentially expensive database calls.

## The `cache_query` Decorator

The `cache_query` decorator is designed to wrap functions that execute read-only database queries. It stores the results of a query in a `query_cache` dictionary, keyed by the SQL query string. Subsequent calls with the same query string will retrieve the result directly from the cache instead of hitting the database again.

### How it Works

```python
query_cache = {} # Global cache dictionary

def cache_query(func):
    """A decorator that caches query results based on the SQL query string."""
    @functools.wraps(func)
    def wrapper(conn, query): # Expects connection and query as arguments
        if query in query_cache:
            print("Fetching from cache")
            return query_cache[query]
        else:
            print("Fetching from database")
            result = func(conn, query) # Execute original function if not in cache
            query_cache[query] = result # Store result in cache
            return result
    return wrapper
```

1.  **`query_cache = {}`**: A global dictionary `query_cache` is used to store the cached results. The query string serves as the key, and the fetched data is the value.

2.  **`cache_query(func)`**: This is the decorator function, taking the database query function (`func`) as an argument.

3.  **`wrapper(conn, query)`**: The inner function. It expects the database connection object (`conn`) and the `query` string as arguments.

4.  **Caching Logic**:
    *   **`if query in query_cache:`**: The `wrapper` first checks if the given `query` string already exists as a key in the `query_cache`.
    *   **Cache Hit**: If the query is found in the cache, it prints "Fetching from cache" and returns the stored result immediately, without executing the actual database query.
    *   **Cache Miss**: If the query is not in the cache, it prints "Fetching from database", executes the original `func` (which performs the database query), stores the `result` in `query_cache` for future use, and then returns the `result`.

### Integration with `with_db_connection`

Similar to other decorators, `cache_query` can be stacked with `with_db_connection` to manage both connection handling and caching efficiently:

```python
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()
```

### Benefits

*   **Performance Optimization:** Significantly reduces database load and query execution time for frequently requested data by serving results from memory.
*   **Reduced Network Traffic:** Fewer round trips to the database server.
*   **Scalability:** Helps the application handle more requests without putting additional strain on the database.
*   **Simplicity:** The caching logic is cleanly encapsulated in a decorator, making it easy to apply to any query function.

### Limitations

*   **Stale Data:** The cached data might become stale if the underlying data in the database changes. This simple cache does not include mechanisms for cache invalidation.
*   **Memory Usage:** Caching too much data can lead to increased memory consumption.
