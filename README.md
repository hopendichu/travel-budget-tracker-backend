# travel-budget-tracker-backend
Backend for the Travel Budget Tracker application
## Features

- User authentication (login, registration, and JWT-based authentication)
- API endpoints for managing travel budgets
- Secure and scalable backend

- Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

7. Start the development server:

    ```bash
    python manage.py runserver
    ```
### API Endpoints

- **User Authentication**:
  - `POST /api/auth/register/`: Register a new user
  - `POST /api/auth/login/`: Log in a user and obtain JWT token
  - `POST /api/auth/logout/`: Log out a user 
