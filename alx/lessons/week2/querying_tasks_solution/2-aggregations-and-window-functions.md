# Documentation for SQL Aggregations and Window Functions

This document explains the SQL queries in the `database-adv-script/aggregations_and_window_functions.sql` file. These queries demonstrate the use of aggregation and window functions to perform calculations and rankings on the data.

## Aggregations and Window Functions

### 1. Aggregation with `COUNT` and `GROUP BY`

*   **Query:**
    ```sql
    SELECT
        u.user_id,
        u.first_name,
        u.last_name,
        COUNT(b.booking_id) AS total_bookings
    FROM
        User u
    LEFT JOIN
        Booking b ON u.user_id = b.user_id
    GROUP BY
        u.user_id,
        u.first_name,
        u.last_name
    ORDER BY
        total_bookings DESC;
    ```
*   **Explanation:**
    *   This query calculates the total number of bookings made by each user.
    *   It uses a `LEFT JOIN` to include all users, even those who have not made any bookings.
    *   The `COUNT(b.booking_id)` function counts the number of bookings for each user.
    *   The `GROUP BY` clause groups the rows by user, so that `COUNT` calculates the bookings for each individual user.
    *   The results are ordered by the total number of bookings in descending order.

### 2. Window Function with `RANK`

*   **Query:**
    ```sql
    WITH PropertyBookingCounts AS (
        SELECT
            p.property_id,
            p.name,
            COUNT(b.booking_id) AS booking_count
        FROM
            Property p
        LEFT JOIN
            Booking b ON p.property_id = b.property_id
        GROUP BY
            p.property_id,
            p.name
    )
    SELECT
        property_id,
        name,
        booking_count,
        RANK() OVER (ORDER BY booking_count DESC) AS property_rank
    FROM
        PropertyBookingCounts
    ORDER BY
        property_rank;
    ```
*   **Explanation:**
    *   This query ranks properties based on the number of bookings they have received.
    *   It uses a Common Table Expression (CTE) named `PropertyBookingCounts` to first calculate the number of bookings for each property.
    *   The `RANK()` window function is then used to assign a rank to each property based on its `booking_count` in descending order. Properties with the same number of bookings will receive the same rank.
    *   The final result shows the property, its booking count, and its rank.
