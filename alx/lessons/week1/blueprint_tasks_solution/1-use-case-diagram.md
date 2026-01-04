# Documentation for Airbnb Clone Use Case Diagram

This document explains the use case diagram for the Airbnb Clone backend, as detailed in the `use-case-diagram/README.md` file. The diagram is represented textually, outlining the actors in the system and the actions they can perform.

## 1. Actors

The system has several actors, each with a distinct role:

*   **Guest:** A user who is looking to book a property.
*   **Host:** A user who lists and manages properties.
*   **Admin:** A superuser who has oversight of the entire platform.
*   **System:** The backend application itself, which handles automated processes.
*   **Payment Gateway:** An external service for processing payments.
*   **Email Service:** An external service for sending notifications.

## 2. Use Cases

The use cases describe the interactions between the actors and the system.

### 2.1. Guest Use Cases

A guest's primary interactions are focused on finding and booking properties:

*   **Account Management:** Register, log in, and manage their profile.
*   **Property Search:** Search for properties and filter the results.
*   **Booking:** Book a property, which includes payment processing.
*   **Post-Stay:** Cancel bookings and leave reviews for properties.
*   **Notifications:** Receive email updates about their bookings.

### 2.2. Host Use Cases

A host's interactions are centered around managing their properties and bookings:

*   **Account Management:** Register, log in, and manage their profile.
*   **Property Management:** Create, update, and delete property listings.
*   **Booking Management:** View and manage bookings for their properties, including cancellations.
*   **Reviews:** Respond to reviews left by guests.
*   **Payments:** Receive payouts for completed bookings.
*   **Notifications:** Receive email updates about their bookings.

### 2.3. Admin Use Cases

An admin has the highest level of access and is responsible for platform management:

*   **Dashboard Access:** Log in to the admin dashboard.
*   **Management:** Manage users, property listings, and bookings.
*   **Monitoring:** Monitor payment transactions.

### 2.4. System Use Cases

The system performs several automated tasks:

*   **Payment Processing:** Interacts with the payment gateway to handle payments.
*   **Email Notifications:** Sends out emails for various events.
*   **Data Validation:** Ensures all data submitted by users is valid.
*   **Authentication and Authorization:** Verifies user identity and permissions.
