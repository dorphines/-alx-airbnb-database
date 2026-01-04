# Documentation for Airbnb Clone Data Flow Diagram (DFD)

This document explains the Data Flow Diagram (DFD) for the Airbnb Clone backend, as detailed in the `data-flow-diagram/data-flow.md` file. The DFD is represented textually and describes how data moves through the system.

## Data Flow Diagram Overview

The DFD is presented in two levels:

*   **Level 0 (Context Diagram):** This provides a high-level overview of the entire system as a single process and its interactions with external entities.
*   **Level 1 (Detailed DFD):** This breaks down the system into smaller, more detailed processes and shows how data flows between them.

## Level 0: Context Diagram

At this level, the entire Airbnb Clone backend is treated as a single black box. It shows the data that flows between the system and the outside world.

*   **External Entities:** These are the users and services that interact with the system:
    *   Guest
    *   Host
    *   Admin
    *   Payment Gateway
    *   Email Service
*   **Data Flows:** This represents the data being exchanged. For example, a `Guest` sends `Booking Requests` to the system, and the `System` sends `Booking Confirmations` back.

## Level 1: Detailed DFD

This level provides a more detailed look inside the backend system, breaking it down into its main processes.

*   **Processes:** These are the main functions of the backend:
    1.  **User Management:** Handles user registration, login, and profile updates.
    2.  **Property Management:** Manages the creation, updating, and deletion of property listings.
    3.  **Booking Management:** Handles all aspects of booking a property.
    4.  **Payment System:** Processes payments for bookings.
    5.  **Notification System:** Sends out emails and other notifications.
    6.  **Review System:** Manages reviews and ratings for properties.

*   **Data Stores:** These are where the system's data is stored:
    *   `Users`
    *   `Properties`
    *   `Bookings`
    *   `Payments`
    *   `Reviews`

*   **Data Flows:** This shows how data moves between the processes and data stores. For example, a `Booking Request` from a `Guest` goes to the `Booking Management` process, which then stores the booking information in the `Bookings` data store. When a booking is confirmed, the `Booking Management` process sends a request to the `Notification System` to send a confirmation email.
