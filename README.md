# Student API - Django REST Framework (DRF)

This project is a Django-based REST API for managing student data. It supports CRUD operations (Create, Read, Update, Delete) using HTTP methods like `GET`, `POST`, `PATCH`, `PUT`, and `DELETE`.

---

## Project Structure
```bash 
first_drf_project/
|-- basic_authentication/         # Implements authentication using Django's built-in authentication system
|-- class_based_views/            # Contains CBVs (Class-Based Views) for handling student API requests
|-- custom_permission/            # Custom permissions for restricting API access
|-- first_drf_project/            # Core Django project settings and configurations
|   |-- __pycache__/              # Compiled Python files for optimization
|   |-- __init__.py               # Marks this directory as a Python package
|   |-- asgi.py                   # ASGI entry point for the project
|   |-- settings.py               # Project settings, including installed apps, middleware, and database configuration
|   |-- urls.py                   # URL routing for the project
|   |-- wsgi.py                   # WSGI entry point for the project
|-- function_based_api_view/      # Implements API using function-based views (FBVs)
|-- generic_api/                  # Contains generic API views for simplified CRUD operations
|-- generic_views/                # Implements generic class-based views
|-- model_viewsets/               # Viewsets implementation using Django REST Framework (DRF)
|-- session_authentication/       # Implements session-based authentication
|-- student_drf_extra/            # Additional utilities related to student APIs
|-- students/                     # Contains models, serializers, and views for Student API
|-- viewsets/                     # Implements ViewSets for handling API endpoints
|-- db.sqlite3                     # SQLite database storing application data
|-- manage.py                      # Django's command-line utility for administrative tasks
```

---

## Endpoints

### 1. `GET` - Retrieve Student Data
- **URL**: `/student_api/`
- **Request Body**:
  ```json
  {
    "id": 1
  }
    ```
- If an `id` is provided, the API returns data for the specific student.
- If no `id` is provided, the API returns all student data.

### 2. `POST` - Create a New Student Entry
- **URL**: `/student_api/`
- **Request Body**:
```json
{
  "name": "John",
  "roll": 101,
  "age": 21,
  "city": "New York"
}
```
- Creates a new student entry in the database.
- Returns a success message if the operation is successful.

### 3. `PATCH` - Partially Update Student Data
- **URL**: `/student_api/`
- **Request Body**:
```json
{
  "id": 1,
  "name": "John Updated"
}
```
- Updates only the provided fields for the student with the given `id`.

### 3. `PUT` - Finally Update Student Data
- **URL**: `/student_api/`
- **Request Body**:
```json
{
  "id": 1,
  "name": "John Updated",
  "roll": 102,
  "age": 22,
  "city": "Los Angeles"
}
```
- Fully replaces the student data for the given `id`.

### 3. `DELETE` - Delete Student Data
- **URL**: `/student_api/`
- **Request Body**:
```json
{
  "id": 1,
}
```
- Deletes the student with the given `id`.

---

### Notes
- **CSRF Exemption:** The `@csrf_exempt` decorator is used to allow external requests.
- **Authentication:** Supports basic authentication, session authentication, and custom permissions.
- **Modular Design:** Organized into multiple Django apps for better maintainability.

---

## Installation and Setup

Follow these instructions to set up and run the project locally:

---

### 1. Clone the Repository
```bash
# Clone the repository
git clone <repository_url>

# Navigate to the project folder
cd <repository_folder>
```

---

### 2. Create and Activate a Virtual Environment
## On Windows
```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
.\env\Scripts\activate
```

## On MacOS/Linux:
```bash
# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate
```

---

### 3. Install Requirements
```bash
# Install all dependencies listed in requirements.txt
pip install -r requirements.txt
```

---

### 4. Apply Migrations
```bash
python manage.py migrate
```

---

### 5. Run the Development Server
```bash
python manage.py runserver
```

---

### 6. Access the Application
```bash
http://127.0.0.1:8000/
```

---
