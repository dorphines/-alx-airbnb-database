# Documentation for User Registration Flowchart

This document explains the flowchart for the user registration process in the Airbnb Clone backend, as detailed in the `flowcharts/user-registration-flowchart.md` file. The flowchart is represented textually and outlines the step-by-step process for registering a new user.

## User Registration Process Flow

The flowchart illustrates the following sequence of events when a new user signs up:

1.  **Initiation:** The process starts when a user decides to register and navigates to the registration page.

2.  **Data Submission:** The user fills out the registration form with their name, email, password, and role (Guest or Host) and submits it.

3.  **Data Validation:** The system first validates the submitted data. If the data is not in the correct format (e.g., an invalid email address), an error message is shown, and the process waits for the user to resubmit the form with corrected information.

4.  **Check for Duplicates:** If the data is valid, the system checks if a user with the same email address already exists in the database. If so, an error is displayed to prevent duplicate accounts.

5.  **Password Hashing:** To ensure security, the user's password is not stored in plain text. It is "hashed" into a long, irreversible string of characters.

6.  **User Creation:** The new user's information (including the hashed password) is saved to the database.

7.  **Session Creation:** A JSON Web Token (JWT) is generated for the user. This token will be used to keep the user logged in and to authenticate their future requests.

8.  **Welcome Email:** The system sends a welcome email to the user. The flowchart includes a check to see if the email was sent successfully and logs a failure if it was not. This step is not critical to the registration itself, so the process continues even if the email fails to send.

9.  **Redirection:** Finally, the user is redirected to their dashboard, and the registration process is complete.
