# Documentation for Airbnb Clone Database Seeding

This document explains the SQL script for seeding the Airbnb Clone database with sample data, as detailed in the `database-script-0x02/seed.sql` file. Seeding is the process of populating a database with an initial set of data, which is useful for testing and development purposes.

## Database Seeding Script

The `seed.sql` script contains a series of `INSERT INTO` statements that add sample data to the tables created by the `schema.sql` script.

### Purpose of Seeding

The primary purposes of seeding the database are:

*   **Testing:** To test the functionality of the application with a realistic set of data.
*   **Development:** To provide developers with data to work with when building and testing new features.
*   **Demonstration:** To showcase the application's features with pre-populated content.

### Sample Data

The `seed.sql` script inserts the following sample data:

*   **Users:**
    *   Creates a few sample users with different roles: a `guest`, a `host`, and an `admin`.

*   **Properties:**
    *   Adds a couple of properties listed by the sample `host`.

*   **Bookings:**
    *   Creates bookings for the properties, made by the sample `guest`. The bookings have different statuses (`confirmed` and `pending`).

*   **Payments:**
    *   Adds a payment record for one of the confirmed bookings.

*   **Reviews:**
    *   Inserts a sample review from the `guest` for one of the properties.

*   **Messages:**
    *   Adds a sample message from the `guest` to the `host`.

This initial data set provides a foundation for testing the core features of the Airbnb Clone application, such as user authentication, property listing, booking, and messaging.
