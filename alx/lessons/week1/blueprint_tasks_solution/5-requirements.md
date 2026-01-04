# Documentation for Airbnb Clone Backend Requirement Specifications

This document explains the requirement specifications for the Airbnb Clone backend, as detailed in the `requirements.md` file. These specifications outline the functional and technical requirements for three key features of the backend.

## 1. User Authentication

This feature is responsible for managing user accounts and securing the application.

*   **Functional Requirements:**
    *   Users can register with an email, password, and role (Guest/Host).
    *   Registered users can log in to their accounts.
    *   The system uses JSON Web Tokens (JWT) for session management.
    *   Access to certain parts of the application is restricted to authenticated users.

*   **API Endpoints:**
    *   `POST /api/auth/register`: To create a new user account.
    *   `POST /api/auth/login`: To log in an existing user.

*   **Validation Rules:**
    *   The specifications define rules for the data submitted during registration, such as a unique email, a strong password, and a valid role.

## 2. Property Management

This feature allows hosts to manage their property listings.

*   **Functional Requirements:**
    *   Hosts can create, update, and delete their property listings.
    *   All users can view property listings.
    *   The system stores comprehensive details about each property.

*   **API Endpoints:**
    *   `POST /api/properties`: To create a new property listing.
    *   `GET /api/properties/:id`: To retrieve a single property.
    *   `PUT /api/properties/:id`: To update a property.
    *   `DELETE /api/properties/:id`: To delete a property.

*   **Validation Rules:**
    *   Rules are in place to ensure that property listings have a title, description, price, and location.

## 3. Booking System

This feature handles the process of booking a property.

*   **Functional Requirements:**
    *   Guests can book a property for a specific date range.
    *   The system prevents double-bookings.
    *   Both guests and hosts can cancel bookings.

*   **API Endpoints:**
    *   `POST /api/bookings`: To create a new booking.
    *   `GET /api/bookings`: To retrieve a list of bookings for a user.
    *   `PUT /api/bookings/:id/cancel`: To cancel a booking.

*   **Validation Rules:**
    *   The system validates that a booking has a valid property ID and that the check-in and check-out dates are logical.
