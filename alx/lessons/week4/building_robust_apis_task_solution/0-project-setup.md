# Documentation for Project Setup

This document confirms the completion of the project setup for the Django messaging application, as outlined in the `building_robust_apis_task`. The setup involves initializing a Django project, installing and configuring Django REST Framework, and creating a messaging app.

## Project Structure

The project has the following directory structure, confirming that the initial setup steps have been completed:

```
repos/alx-backend-python/messaging_app/
├── chats/                     # Django app for messaging functionality
├── messaging_app/             # Main Django project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Project settings
│   ├── urls.py                # Project-wide URL configurations
│   └── wsgi.py
├── db.sqlite3                 # SQLite database file
├── manage.py                  # Django's command-line utility
└── postman_collections.json   # Postman collections for API testing
```

## Django REST Framework Configuration

The `messaging_app/settings.py` file confirms that Django REST Framework (DRF) is correctly set up:

*   **`INSTALLED_APPS`**:
    *   `'rest_framework'` is included, enabling DRF.
    *   `'rest_framework_simplejwt'` is included for JSON Web Token (JWT) based authentication.
    *   `'chats'` is included, indicating that the custom messaging app is registered.
    *   `'django_filters'` is included, which is often used with DRF for filtering API results.

*   **`REST_FRAMEWORK` Dictionary**:
    *   `'DEFAULT_AUTHENTICATION_CLASSES'`: Configured to use `JWTAuthentication`, ensuring secure API access.
    *   `'DEFAULT_PERMISSION_CLASSES'`: Set to `IsAuthenticated`, meaning only authenticated users can access the API endpoints by default.

*   **`AUTH_USER_MODEL`**:
    *   `AUTH_USER_MODEL = 'chats.User'` is set, indicating that a custom `User` model defined within the `chats` app will be used for authentication. This is a common practice in Django projects to extend user functionality.

In summary, the foundational project setup for the Django REST API is complete and properly configured for developing robust messaging functionalities.
