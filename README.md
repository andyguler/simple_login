# SQLite Login and Sign-Up System

This script demonstrates a basic login and sign-up system using **SQLite** as the database. Users can sign up by creating an account with their email and password or log in to their existing account.

---

## Table of Contents

1. [About](#about)
2. [Features](#features)
3. [Setup Instructions](#setup-instructions)
4. [How to Use](#how-to-use)
5. [Contributing](#contributing)
6. [License](#license)

---

## About

The **SQLite Login and Sign-Up System** allows users to interact with an SQLite database to either create an account or log in. The database stores user credentials (email and password) securely.

---

## Features

- **Sign-Up Functionality**:
  - Ensures email validity.
  - Checks if the email already exists in the database.
  - Saves new user credentials.

- **Login Functionality**:
  - Validates user credentials against the database.
  - Displays appropriate error messages for invalid input.

- **Data Persistence**:
  - Uses an SQLite database (`tutorial.db`) to store and retrieve user credentials.

---

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/<your-username>/sqlite-login-system.git
    cd sqlite-login-system
    ```

2. **Prepare the SQLite database**:
    Open a Python shell or use an SQLite client to create the required `Login` table:
    ```sql
    CREATE TABLE Login (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
    ```

3. **Run the script**:
    Ensure you have Python installed, then execute:
    ```bash
    python login_system.py
    ```

---

## How to Use

1. **Sign Up**:
   - Choose `0` when prompted.
   - Enter a valid email address.
   - Provide a password.
   - If successful, the account is created, and you can log in.

2. **Log In**:
   - Choose `1` when prompted.
   - Enter your email address.
   - Enter your password.
   - If the credentials are valid, you will be logged in successfully.

3. **Error Handling**:
   - Invalid email format: The system prompts you to enter a valid email.
   - Duplicate email during sign-up: A warning is displayed.
   - Incorrect password: The system notifies you.

---
