# Documentation for SQL Subqueries

This document explains the SQL queries in the `database-adv-script/subqueries.sql` file. These queries demonstrate the use of both non-correlated and correlated subqueries to perform more complex data retrieval.

## SQL Subqueries

A subquery is a query nested inside another query. They are useful for breaking down complex queries into smaller, more manageable parts.

### 1. Non-Correlated Subquery

*   **Query:**
    ```sql
    SELECT
        p.property_id,
        p.name,
        p.description,
        p.location
    FROM
        Property p
    WHERE
        p.property_id IN (
            SELECT
                r.property_id
            FROM
                Review r
            GROUP BY
                r.property_id
            HAVING
                AVG(r.rating) > 4.0
        );
    ```
*   **Explanation:**
    *   This query finds all properties that have an average rating greater than 4.0.
    *   It uses a non-correlated subquery, which is a subquery that can be run independently of the outer query.
    *   The inner query first calculates the average rating for each property and returns a list of `property_id`s for properties with an average rating greater than 4.0.
    *   The outer query then selects all properties whose `property_id` is in the list returned by the inner query.

### 2. Correlated Subquery

*   **Query:**
    ```sql
    SELECT
        u.user_id,
        u.first_name,
        u.last_name,
        u.email
    FROM
        User u
    WHERE
        (
            SELECT
                COUNT(b.booking_id)
            FROM
                Booking b
            WHERE
                b.user_id = u.user_id
        ) > 3;
    ```
*   **Explanation:**
    *   This query finds all users who have made more than 3 bookings.
    *   It uses a correlated subquery, which is a subquery that depends on the outer query for its values.
    *   For each user processed by the outer query, the inner query is executed once to count the number of bookings made by that specific user (`b.user_id = u.user_id`).
    *   The `WHERE` clause of the outer query then checks if the count returned by the inner query is greater than 3.
