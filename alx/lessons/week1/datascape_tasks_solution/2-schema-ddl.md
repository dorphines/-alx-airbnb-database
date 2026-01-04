# Documentation for Airbnb Clone Database Schema (DDL)

This document explains the SQL Data Definition Language (DDL) script for creating the Airbnb Clone database schema, as detailed in the `database-script-0x01/schema.sql` file. The DDL script defines the structure of the database, including the tables, columns, data types, constraints, and indexes.

## SQL DDL Script

The `schema.sql` script contains a series of `CREATE TABLE` statements that build the database. Here's a breakdown of what the script does:

### 1. Table Creation

The script creates the following tables:

*   **User:** Stores information about users, including their credentials and role.
*   **Property:** Contains details about the properties listed on the platform.
*   **Booking:** Keeps track of all property bookings.
*   **Payment:** Records payments made for bookings.
*   **Review:** Stores reviews and ratings for properties.
*   **Message:** Holds messages sent between users.

Each `CREATE TABLE` statement specifies the columns for that table, along with their data types and any constraints.

### 2. Constraints

The script uses several types of constraints to ensure data integrity:

*   **PRIMARY KEY:** Each table has a primary key column (`user_id`, `property_id`, etc.) that uniquely identifies each record.
*   **FOREIGN KEY:** These constraints create relationships between tables. For example, the `host_id` in the `Property` table is a foreign key that references the `user_id` in the `User` table, ensuring that every property has a valid host.
*   **UNIQUE:** The `email` column in the `User` table has a `UNIQUE` constraint to prevent duplicate email addresses.
*   **NOT NULL:** This constraint ensures that a column cannot have a `NULL` value.
*   **CHECK:** The `rating` column in the `Review` table has a `CHECK` constraint to ensure that the rating is between 1 and 5.
*   **ENUM:** The `role` column in the `User` table and the `status` column in the `Booking` table use an `ENUM` data type to restrict the values to a predefined set.

### 3. Indexes

The script also creates several indexes on the tables:

*   **`CREATE INDEX`:** These statements create indexes on columns that are frequently used in search conditions, such as `email` in the `User` table and foreign key columns.
*   **Purpose of Indexes:** Indexes help to speed up the performance of `SELECT` queries by providing a faster way for the database to find the data it's looking for.
