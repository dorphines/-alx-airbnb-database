# Documentation for SQL Joins Queries

This document explains the SQL queries in the `database-adv-script/joins_queries.sql` file. These queries demonstrate the use of different types of SQL joins to retrieve data from multiple tables in the Airbnb Clone database.

## SQL Joins

SQL joins are used to combine rows from two or more tables based on a related column between them.

### 1. INNER JOIN

*   **Query:**
    ```sql
    SELECT
        b.booking_id,
        b.start_date,
        b.end_date,
        u.first_name,
        u.last_name,
        u.email
    FROM
        Booking b
    INNER JOIN
        User u ON b.user_id = u.user_id;
    ```
*   **Explanation:**
    *   This query uses an `INNER JOIN` to combine the `Booking` and `User` tables.
    *   It retrieves all bookings along with the details of the user who made each booking.
    *   An `INNER JOIN` only returns rows where the join condition is met, so bookings without a user or users without a booking will not be included.

### 2. LEFT JOIN

*   **Query:**
    ```sql
    SELECT
        p.property_id,
        p.name AS property_name,
        r.rating,
        r.comment
    FROM
        Property p
    LEFT JOIN
        Review r ON p.property_id = r.property_id;
    ```
*   **Explanation:**
    *   This query uses a `LEFT JOIN` to combine the `Property` and `Review` tables.
    *   It retrieves all properties and their reviews.
    *   The `LEFT JOIN` ensures that all properties are included in the result, even if they have no reviews. For properties without reviews, the `rating` and `comment` columns will be `NULL`.

### 3. FULL OUTER JOIN

*   **Query:**
    ```sql
    SELECT
        u.user_id,
        u.first_name,
        u.last_name,
        b.booking_id,
        b.start_date,
        b.end_date
    FROM
        User u
    FULL OUTER JOIN
        Booking b ON u.user_id = b.user_id;
    ```
*   **Explanation:**
    *   This query uses a `FULL OUTER JOIN` to combine the `User` and `Booking` tables.
    *   It retrieves all users and all bookings.
    *   If a user has not made any bookings, their booking details will be `NULL`.
    *   If a booking is not associated with any user, its user details will be `NULL`.
    *   This type of join is useful for seeing all data from both tables, regardless of whether there is a match in the other table.
