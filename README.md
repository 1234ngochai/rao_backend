# Rao Backend Server

A backend server for the Rao application, built with Django and Django REST Framework.

## Features

- User registration and authentication
- Custom user model with custom user manager
- RESTful API endpoints for user management
- Admin interface for managing users

## Prerequisites

- Python 3.6 or higher
- Git

## Installation

Follow these steps to set up the Rao backend server on your local machine.

### 1. Clone the Repository

Clone the project from GitHub and navigate into the project directory:

```bash
git clone https://github.com/yourusername/rao-backend.git
cd rao-backend
```

### 2. Set Up a Virtual Environment

Create a virtual environment to isolate the project dependencies:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Activate the virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

Install the required dependencies from the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

Set up the database by applying the necessary migrations:

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

To access the Django admin panel, you can create a superuser by running the following command:

```bash
python manage.py createsuperuser
```

Follow the prompts to create a username, email, and password.

### 7. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The server will start running on [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## API Testing

You can use Postman to test the API endpoints. Below is an example of how to test the user registration endpoint:

### 1. User Registration

**Endpoint:** `POST /api/users/register/`

**Request Body (JSON):**

```json
{
  "username": "User5",
  "password": "testpass123"
}
```

**Response Example:**

```json
{
  "id": 5,
  "username": "User5"
}
```

## License

This project is licensed under the MIT License.
