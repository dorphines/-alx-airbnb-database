# Documentation for `2-lazy_paginate.py`

This document explains the `2-lazy_paginate.py` script, which demonstrates how to use a Python generator to lazily load paginated data from a MySQL database.

## Lazy Loading with Generators

This script provides two functions that work together to implement lazy loading of paginated data. Lazy loading is a design pattern where the loading of an object is deferred until it is needed. This is particularly useful when dealing with large amounts of data, as it avoids loading everything into memory at once.

### `paginate_users(page_size, offset)`

This function fetches a single "page" of users from the `user_data` table.

*   **Parameters:**
    *   `page_size`: The number of users to fetch per page.
    *   `offset`: The starting point from which to fetch the users.
*   **How it Works:**
    1.  It connects to the `ALX_prodev` database.
    2.  It uses the `LIMIT` and `OFFSET` SQL clauses to fetch a specific slice of the user data.
    3.  It returns the fetched rows as a list of dictionaries.

### `lazy_paginate(page_size)`

This is a generator function that yields pages of users one by one, only fetching the next page when it is requested.

*   **How it Works:**
    1.  It uses a `while True` loop to continuously fetch pages.
    2.  In each iteration, it calls the `paginate_users` function to get the next page of users.
    3.  It then `yield`s the fetched page.
    4.  The loop breaks when `paginate_users` returns an empty list, indicating that there are no more users to fetch.
    5.  The `offset` is incremented by the `page_size` in each iteration to get the next chunk of data.

### Usage

The `3-main.py` script shows how to use the `lazy_paginate` generator. It iterates through the pages yielded by `lazy_paginate(100)`, and for each page, it iterates through the users in that page and prints their data. This demonstrates how you can process a large dataset page by page without loading the entire dataset into memory.
