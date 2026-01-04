# Documentation for Table Partitioning

This document explains the concept of table partitioning and how it is applied to the `Booking` table in the Airbnb Clone database to improve performance. The solution is detailed in the `database-adv-script/partitioning.sql` and `database-adv-script/partition_performance.md` files.

## What is Table Partitioning?

Table partitioning is a database optimization technique where a large table is divided into smaller, more manageable pieces called partitions. While the table is still treated as a single logical entity, the data is physically stored in separate partitions.

## Partitioning the `Booking` Table

The `Booking` table is a good candidate for partitioning because it can grow very large over time, and many queries will likely filter bookings by date.

### The Partitioning Strategy

The `Booking` table is partitioned by `RANGE` on the `start_date` column. This means that bookings are grouped into partitions based on their start date. The `partitioning.sql` script provides an example of how to do this in PostgreSQL, creating separate partitions for each year.

```sql
-- Create a new partitioned table
CREATE TABLE Booking_partitioned (
    -- ... columns ...
) PARTITION BY RANGE (start_date);

-- Create partitions for different years
CREATE TABLE Booking_y2024 PARTITION OF Booking_partitioned
    FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');

CREATE TABLE Booking_y2025 PARTITION OF Booking_partitioned
    FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');
```

### Performance Improvements

Partitioning the `Booking` table provides several benefits:

*   **Faster Queries:** When you run a query that filters by `start_date`, the database can use a technique called "partition pruning." This means it only needs to scan the relevant partition(s) instead of the entire table. For example, a query for bookings in June 2025 will only scan the `Booking_y2025` partition, which is much faster than scanning the entire `Booking` table.
*   **Improved Scalability:** As the `Booking` table grows, the performance of date-range queries will not degrade as much as it would with a non-partitioned table.
*   **Easier Maintenance:** Tasks like deleting old data become much easier. For example, to delete all bookings from 2024, you can simply drop the `Booking_y2024` partition, which is an almost instantaneous operation compared to a `DELETE` statement that would have to remove rows one by one.
