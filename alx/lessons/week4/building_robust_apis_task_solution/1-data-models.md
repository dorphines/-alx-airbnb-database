# Documentation for Data Models

This document explains the data models defined in the `messaging_app/chats/models.py` file for the Django messaging application. These models form the core structure of the application's database.

## 1. `User` Model

The `User` model extends Django's `AbstractUser`, providing a customizable user authentication system.

*   **Inherits from:** `AbstractUser`
*   **Fields:**
    *   `id`: Primary Key, `UUIDField`, automatically generated.
    *   `phone_number`: `CharField`, optional phone number.
    *   `role`: `CharField`, defines the user's role (guest, host, admin) with a default of 'guest'.
*   **`__str__` method:** Returns the `username` for string representation.

## 2. `Conversation` Model

The `Conversation` model represents a chat conversation between multiple users.

*   **Fields:**
    *   `id`: Primary Key, `UUIDField`, automatically generated.
    *   `participants`: `ManyToManyField` with the `User` model, indicating all users involved in a conversation. The `related_name='conversations'` allows accessing a user's conversations directly.
    *   `created_at`: `DateTimeField`, automatically set when the conversation is created.
*   **`__str__` method:** Returns a string like "Conversation [id]".

## 3. `Message` Model

The `Message` model represents a single message sent within a conversation.

*   **Fields:**
    *   `id`: Primary Key, `UUIDField`, automatically generated.
    *   `conversation`: `ForeignKey` to the `Conversation` model. If a conversation is deleted, all its messages are also deleted (`on_delete=models.CASCADE`). The `related_name='messages'` allows accessing messages within a conversation.
    *   `sender`: `ForeignKey` to the `User` model, indicating who sent the message. If a user is deleted, their sent messages are also deleted. The `related_name='sent_messages'` allows accessing messages sent by a user.
    *   `message_body`: `TextField`, stores the content of the message.
    *   `sent_at`: `DateTimeField`, automatically set when the message is sent.
*   **`__str__` method:** Returns a string like "Message from [sender] at [sent_at]".

## Relationships

*   **User to Conversation:** Many-to-many relationship (`participants` field in `Conversation`). A user can be part of many conversations, and a conversation can have many participants.
*   **Conversation to Message:** One-to-many relationship (`conversation` field in `Message`). A conversation can have many messages, but each message belongs to only one conversation.
*   **User to Message:** One-to-many relationship (`sender` field in `Message`). A user can send many messages, but each message is sent by only one user.
