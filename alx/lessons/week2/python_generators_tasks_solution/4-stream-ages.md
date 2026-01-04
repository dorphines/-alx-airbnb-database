# Documentation for `4-stream_ages.py`

This document explains the `4-stream_ages.py` script, which demonstrates how to use a Python generator to perform a memory-efficient aggregation (in this case, calculating an average) on a large dataset.

## Memory-Efficient Aggregation

When working with large datasets, loading all the data into memory to perform calculations can be inefficient and may even lead to memory errors. This script shows how to use a generator to process the data one piece at a time, using a constant amount of memory regardless of the dataset's size.

### `stream_user_ages()`

This is a generator function that yields the age of each user from the `user_data` table, one by one.

*   **How it Works:**
    1.  It connects to the `ALX_prodev` database.
    2.  It executes a `SELECT` query to get the `age` of all users.
    3.  It then iterates through the results and `yield`s each age.
    4.  This way, only one age is held in memory at a time within the loop.

### `calculate_average_age()`

This function calculates the average age of all users by using the `stream_user_ages` generator.

*   **How it Works:**
    1.  It initializes two variables, `total_age` and `count`, to 0.
    2.  It then iterates through the ages yielded by `stream_user_ages()`.
    3.  In each iteration, it adds the current `age` to `total_age` and increments the `count`.
    4.  After the loop has finished, it calculates the average by dividing `total_age` by `count`.
    5.  This method allows the calculation to be performed without ever having the full list of ages in memory.

### Main Execution Block

The `if __name__ == "__main__":` block at the end of the script calls the `calculate_average_age()` function and prints the result. This is a standard Python practice to make the script reusable and testable.
