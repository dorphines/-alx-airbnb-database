# Documentation for `1-batch_processing.py`

This document explains the `1-batch_processing.py` script, which contains Python generator functions for fetching and processing user data in batches from a MySQL database.

## Batch Processing with Generators

This script provides two functions that demonstrate how to use generators for efficient batch processing of large datasets.

### `stream_users_in_batches(batch_size)`

This generator function fetches users from the `user_data` table in batches of a specified size.

*   **How it Works:**
    1.  It connects to the `ALX_prodev` database.
    2.  It uses a `while True` loop and SQL's `LIMIT` and `OFFSET` clauses to fetch a specific number of rows (`batch_size`) at a time.
    3.  In each iteration, it `yield`s a batch of users.
    4.  The loop continues until no more rows are returned, at which point it breaks.
    5.  This approach avoids loading the entire table into memory, making it suitable for very large tables.

### `batch_processing(batch_size)`

This function uses the `stream_users_in_batches` generator to process the user data. It filters the users and yields only those who are older than 25.

*   **How it Works:**
    1.  It iterates through the batches yielded by `stream_users_in_batches`.
    2.  For each batch, it iterates through the users in that batch.
    3.  If a user's age is greater than 25, it `yield`s that user.

### Usage

The `2-main.py` script shows how to use the `batch_processing` function. It calls the function with a batch size of 50 and then iterates through the yielded users, printing each one. The `head -n 5` command is used to display only the first 5 results for brevity.
