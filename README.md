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
git clone https://github.com/dzhusjr/TaskManagerAPI.git
cd TaskManagerAPI
```

### 2. Unpack Data Files
Unpack the `data.zip` file into the project root directory. This will create a `data` directory containing the CSV files (`users.csv`, `projects.csv`, and `tasks.csv`).

### 3. Set Up Docker
Make sure Docker is installed and running. Run the following command to build and run the containers:

```bash
docker-compose up --build -d
```

This will:
- Set up a PostgreSQL database.
- Set up the Django application server using Gunicorn.

### 4. Run Migrations
After the containers are up and running, run the database migrations:

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### 5. Import CSV Data
Run the custom management command to import data from CSV files:

```bash
docker-compose exec web python manage.py import_users
docker-compose exec web python manage.py import_tasks
docker-compose exec web python manage.py import_projects
```

This will import data from `users.csv`, `projects.csv`, and `tasks.csv` stored in the `data` directory.

### 6. Access the Application
- The API should be available at `http://localhost:8000/`.
- Use tools like Postman or cURL to interact with the API.

## API Endpoints
### User Management
- **List Users**: `GET /api/users/`
- **Retrieve User**: `GET /api/users/{id}/`
- **Delete User**: `DELETE /api/users/{id}/` (requires password)
- **Create User**: `POST /api/users/`
- **Update User**: `PATCH /api/users/{id}/` (partial update)

### Project Management
- **List Projects**: `GET /api/projects/`
- **Retrieve Project**: `GET /api/projects/{id}/`
- **Delete Project**: `DELETE /api/projects/{id}/`
- **Create Project**: `POST /api/projects/`
- **Update Project**: `PATCH /api/projects/{id}/` (partial update)
- **Add User to Project**: `POST /api/projects/{id}/add_user/` (requires user email)
- **Add Task to Project**: `POST /api/projects/{id}/add_task/` (requires task id)

### Task Management
- **List Tasks**: `GET /api/tasks/`
- **View Tasks by Project**: `GET /api/tasks/by_project/?project_id={id}&email={user_email}` (only users assigned to the project can view)

## Notes
- The project uses **Docker** for containerization.
- The project follows **PEP-8** standards.
- Ensure all sensitive data is managed through the `.env` file.
