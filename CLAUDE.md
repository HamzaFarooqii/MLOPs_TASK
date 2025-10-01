# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flask-based Student Management System with clean architecture. The application uses Flask backend with in-memory storage and Flask frontend with Jinja2 templates. Users can submit student information (name, roll number, university) through a web form and view all submitted records in a table below.

## Architecture

### Project Structure
```
├── backend/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── student.py           # Student data model
│   │   └── storage.py           # In-memory storage singleton
│   ├── validators/
│   │   ├── __init__.py
│   │   └── student_validator.py # Input validation functions
│   ├── app.py                   # Flask backend API server
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── templates/
│   │   └── index.html           # Main HTML template
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css        # All styling
│   │   └── js/
│   │       └── app.js           # Client-side JavaScript
│   ├── app.py                   # Flask frontend server
│   ├── requirements.txt
│   └── Dockerfile
└── docker-compose.yml           # Multi-container orchestration
```

### Key Design Patterns

**Flask Stack Architecture**:
- **Backend**: Flask REST API server (Python)
- **Frontend**: Flask web server with Jinja2 templates (Python)
- **Storage**: In-memory Python class (no database)

**RESTful API**: Clean API endpoints following REST principles:
- `GET /api/students` - Fetch all students
- `POST /api/students` - Add new student

**Validation**: Python regex-based validation for robust input checking on the backend.

**Separation of Concerns**:
- **Backend** ([backend/](backend/)): API server, business logic, data management
- **Frontend** ([frontend/](frontend/)): User interface, client-side logic, proxies requests to backend
- **Models** ([backend/models/](backend/models/)): Data structures (Student, Storage)
- **Validators** ([backend/validators/](backend/validators/)): Input validation logic
- **Templates** ([frontend/templates/](frontend/templates/)): Jinja2 HTML templates
- **Static** ([frontend/static/](frontend/static/)): CSS and JavaScript files

### Data Flow
1. User fills form in HTML template
2. JavaScript sends HTTP POST to frontend `/api/students`
3. Frontend proxies request to backend `/api/students`
4. Backend validator validates input using regex patterns
5. Backend creates Student model instance
6. Backend stores in Storage singleton
7. Backend returns success response
8. Frontend proxies response back to client
9. JavaScript fetches updated list → GET `/api/students`
10. JavaScript re-renders table with new data

## Commands

### Setup and Installation

#### Backend
```bash
cd backend
pip install -r requirements.txt
```

#### Frontend
```bash
cd frontend
pip install -r requirements.txt
```

### Running the Application

#### With Docker (Recommended)
```bash
# Build and run both frontend and backend
docker-compose up --build

# Run with live reload (watch mode for development)
docker compose watch

# Stop all services
docker-compose down
```

**Access:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

#### Without Docker

**Terminal 1 - Backend:**
```bash
cd backend
python app.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
python app.py
```

### Docker Watch Mode
The `docker compose watch` command enables live updates during development:
- **Backend**: Changes to `backend/` Python files are synced automatically
- **Frontend**: Changes to `frontend/` files (templates, static, app.py) are synced
- **Rebuild**: Changes to `requirements.txt` trigger container rebuild
- Python auto-reload works in development mode

## Input Validation Rules

Implemented in [backend/validators/student_validator.py](backend/validators/student_validator.py):

- **Name**:
  - Required, 2-100 characters
  - Only letters, spaces, hyphens, and periods allowed
  - Regex: `^[a-zA-Z\s\-\.]+$`

- **Roll Number**:
  - Required, 1-50 characters
  - Only alphanumeric characters, hyphens, and underscores allowed
  - Regex: `^[a-zA-Z0-9\-_]+$`

- **University**:
  - Required, 3-200 characters
  - Allows alphanumeric, spaces, and common punctuation
  - Regex: `^[a-zA-Z0-9\s\-\.\,&\']+$`

## Error Handling

- **Python Validation**: Server-side validation with detailed error messages
- **Try-Except Blocks**: Comprehensive exception handling in routes
- **HTTP Status Codes**: Proper use of 200, 201, 400, 404, 500 status codes
- **Flash Messages**: User feedback for success/error states via JavaScript
- **Auto-dismiss**: Flash messages auto-dismiss after 5 seconds

## Storage

Currently uses in-memory storage via [backend/models/storage.py](backend/models/storage.py). Data persists only during application runtime. To add MongoDB or PostgreSQL:
1. Install appropriate Python driver (`pymongo` or `psycopg2`)
2. Create database connection
3. Replace Storage.py with database models
4. Add database service to docker-compose.yml

## API Endpoints

### GET /api/students
Returns all students
```json
{
  "success": true,
  "data": [
    {
      "id": "1234567890",
      "name": "John Doe",
      "rollNo": "CS-2021-001",
      "university": "MIT"
    }
  ]
}
```

### POST /api/students
Add new student
**Request:**
```json
{
  "name": "John Doe",
  "rollNo": "CS-2021-001",
  "university": "MIT"
}
```
**Response:**
```json
{
  "success": true,
  "message": "Student record added successfully!",
  "data": { ... }
}
```

## Frontend Architecture

The frontend is a Flask application that serves as both:
1. **Web Server**: Serves HTML templates and static files
2. **API Proxy**: Forwards API requests from browser to backend

This architecture allows:
- Clean separation between frontend UI and backend API
- Easy CORS handling via proxy
- Single-page application feel with server-side templating
