# Documentation for Indexing and Performance Optimization

This document explains the process of implementing indexes to optimize query performance in the Airbnb Clone database, as detailed in the `database-adv-script/index_performance.md` file.

## The Importance of Indexing

In a database, an index is a data structure that improves the speed of data retrieval operations on a table at the cost of additional writes and storage space to maintain the index data structure. Indexes are used to quickly locate data without having to search every row in a database table every time a table is accessed.

## Identifying Columns for Indexing

The first step in optimization is to identify which columns are frequently used in `WHERE` clauses, `JOIN` conditions, or `ORDER BY` clauses. For the Airbnb database, the following columns were identified as good candidates for indexing:

*   **`User(first_name, last_name)`**: To speed up searches for users by their name.
*   **`Property(host_id)`**: To improve the performance of joins between `Property` and `User` tables.
*   **`Property(location)`**: To make location-based searches for properties faster.
*   **`Booking(start_date, end_date)`**: To optimize queries that filter bookings by a date range.

## Creating Indexes

The following `CREATE INDEX` statements are used to create the indexes on these columns:

```sql
CREATE INDEX idx_user_name ON User(first_name, last_name);
CREATE INDEX idx_property_host_id ON Property(host_id);
CREATE INDEX idx_property_location ON Property(location);
CREATE INDEX idx_booking_dates ON Booking(start_date, end_date);
```

## Measuring Performance

The `EXPLAIN` or `ANALYZE` commands in SQL can be used to see how the database will execute a query.

*   **Before Indexing:** A query on a non-indexed column will typically result in a "Sequential Scan," meaning the database has to read through every row in the table.
*   **After Indexing:** After an index is created, the query plan will change to an "Index Scan." This is much more efficient because the database can use the index to directly find the required data.

By implementing these indexes, the overall performance of the application can be significantly improved, especially as the amount of data grows.
