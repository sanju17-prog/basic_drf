# basic_drf
# Student API

This project is a Django-based REST API for managing student data. It supports CRUD operations (Create, Read, Update, Delete) using HTTP methods like `GET`, `POST`, `PATCH`, `PUT`, and `DELETE`.

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

### 2. `POST` - Retrieve Student Data
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