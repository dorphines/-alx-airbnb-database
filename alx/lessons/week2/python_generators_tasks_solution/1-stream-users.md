# Documentation for `0-stream_users.py`

This document explains the `0-stream_users.py` script, which contains a Python generator function for streaming user data from a MySQL database.

## `stream_users()` Generator Function

The `stream_users()` function is a generator that fetches user data from the `user_data` table one row at a time. This is a memory-efficient way to process large datasets, as it doesn't require loading the entire dataset into memory.

### How it Works

1.  **Database Connection:** The function first connects to the `ALX_prodev` database by calling the `connect_to_prodev()` function from the `seed` module.

2.  **Cursor Creation:** It then creates a cursor with the `dictionary=True` argument. This makes the cursor return rows as dictionaries, where the keys are the column names.

3.  **SQL Execution:** The function executes a `SELECT` query to fetch all rows from the `user_data` table.

4.  **Yielding Rows:** Instead of using `fetchall()` to get all the rows at once, the function iterates over the cursor object. In each iteration, it `yield`s a single row. The `yield` keyword is what makes this a generator function. It pauses the function's execution and returns the yielded value. When the function is called again, it resumes execution from where it left off.

5.  **Connection Closing:** Finally, the `finally` block ensures that the database connection is closed, even if an error occurs.

### Usage

The `1-main.py` script shows how to use this generator. It iterates over the `stream_users()` generator and prints each user's data. The `itertools.islice()` function is used to limit the output to the first 6 users for demonstration purposes.
