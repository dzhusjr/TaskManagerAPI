# Task Manager Project

## Overview
This is a Task Manager project built with Python and Django REST framework. It allows users to manage tasks, projects, and user accounts, with the following features:
- CSV import for users, projects, and tasks.
- API to create, update, view, and delete users.
- Assign users to projects, with constraints.
- View tasks by project, including pagination.

## Requirements
- Python 3+
- Docker & Docker Compose
- PostgreSQL

## Environment Variables
Create a `.env` file in the root directory with the following content:

```
POSTGRES_USER=<your_postgres_user>
POSTGRES_PASSWORD=<your_postgres_password>
POSTGRES_DB=<your_postgres_db>
SECRET_KEY=<your_django_secret_key>
```

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>
```

### 2. Set Up Docker
Make sure Docker is installed and running. Run the following command to build and run the containers:

```bash
docker-compose up --build
```

This will:
- Set up a PostgreSQL database.
- Set up the Django application server using Gunicorn.

### 3. Run Migrations
After the containers are up and running, run the database migrations:

```bash
docker-compose exec web python manage.py migrate
```

### 4. Import CSV Data
Run the custom management command to import data from CSV files:

```bash
docker-compose exec web python manage.py import_csv
```

This will import data from `users.csv`, `projects.csv`, and `tasks.csv` stored in the `data` directory.

### 5. Access the Application
- The API should be available at `http://localhost:8000/`.
- Use tools like Postman or cURL to interact with the API.

## API Endpoints
### User Management
- **Create User**: `POST /api/users/`
- **Update User**: `PATCH /api/users/{id}/`
- **Delete User**: `DELETE /api/users/{id}/` (requires password)
- **Retrieve User**: `GET /api/users/{id}/`

### Project Management
- **Add User to Project**: `POST /api/projects/{id}/add_user/` (requires user email)

### Task Viewing
- **View Tasks by Project**: `GET /api/tasks/by_project/?project_id={id}&email={user_email}`

## Notes
- The project uses **Gunicorn** as the production server.
- The project follows **PEP-8** standards.
- Ensure all sensitive data is managed through the `.env` file.

## Development
To run the development server locally without Docker:

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   python manage.py runserver
   ```
