# Documentation for Airbnb Clone Database Specifications

This document explains the database specifications for the Airbnb Clone project, as detailed in the `database_specifications_airbnb` file. The specifications outline the structure of the database, including the tables, their columns, and the relationships between them.

## Database Schema

The database is designed to store all the information needed to run the Airbnb Clone application. It consists of the following tables:

### 1. User

This table stores information about the users of the application.

*   **Attributes:**
    *   `user_id`: A unique identifier for each user.
    *   `first_name`, `last_name`, `email`, `password_hash`: Personal information and credentials for the user.
    *   `phone_number`: The user's phone number.
    *   `role`: Defines the user's role in the system (guest, host, or admin).
    *   `created_at`: The date and time when the user account was created.

### 2. Property

This table contains information about the properties listed on the platform.

*   **Attributes:**
    *   `property_id`: A unique identifier for each property.
    *   `host_id`: A reference to the user who owns the property.
    *   `name`, `description`, `location`: Details about the property.
    *   `pricepernight`: The cost to rent the property for one night.
    *   `created_at`, `updated_at`: Timestamps for when the property was created and last updated.

### 3. Booking

This table stores information about property bookings.

*   **Attributes:**
    *   `booking_id`: A unique identifier for each booking.
    *   `property_id`: A reference to the property that was booked.
    *   `user_id`: A reference to the user who made the booking.
    *   `start_date`, `end_date`: The dates for the booking.
    *   `total_price`: The total cost of the booking.
    *   `status`: The current status of the booking (pending, confirmed, or canceled).
    *   `created_at`: The date and time when the booking was made.

### 4. Payment

This table keeps a record of all payments made for bookings.

*   **Attributes:**
    *   `payment_id`: A unique identifier for each payment.
    *   `booking_id`: A reference to the booking for which the payment was made.
    *   `amount`: The amount of the payment.
    *   `payment_date`: The date of the payment.
    *   `payment_method`: The method used for the payment (credit card, PayPal, etc.).

### 5. Review

This table stores reviews left by users for properties.

*   **Attributes:**
    *   `review_id`: A unique identifier for each review.
    *   `property_id`: A reference to the property that was reviewed.
    *   `user_id`: A reference to the user who wrote the review.
    *   `rating`: A numerical rating (1-5).
    *   `comment`: The text of the review.
    *   `created_at`: The date and time when the review was submitted.

### 6. Message

This table stores messages sent between users.

*   **Attributes:**
    *   `message_id`: A unique identifier for each message.
    *   `sender_id`, `recipient_id`: References to the users who sent and received the message.
    *   `message_body`: The content of the message.
    *   `sent_at`: The date and time when the message was sent.

## Constraints and Indexing

*   **Constraints:** The database uses constraints to ensure data integrity. For example, the `email` in the `User` table must be unique, and the `rating` in the `Review` table must be between 1 and 5.
*   **Indexing:** Indexes are used to speed up data retrieval. Primary keys are automatically indexed, and additional indexes are created for frequently searched columns like `email` and `property_id`.
