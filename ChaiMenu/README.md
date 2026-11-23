# ChaiMenu – FastAPI Menu Management API

A simple REST API built using **Python and FastAPI** to retrieve and filter menu items. This project demonstrates FastAPI fundamentals, query parameters, path parameters, Pydantic response models, and HTTP exception handling.

## Features

- Retrieve all menu items.
- Filter menu items by category.
- Retrieve individual menu items using their ID.
- Case-insensitive category filtering.
- Pydantic response validation.
- HTTP 404 handling for unavailable menu items or categories.
- Interactive API documentation using Swagger UI.

## Tech Stack

- **Python**
- **FastAPI**
- **Pydantic**
- **Uvicorn**

## Project Structure

```text
ChaiMenu/
│
├── main.py          # FastAPI application and routes
├── data.py          # Menu items data
├── models.py        # Pydantic models
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/rajeshboya8/ChaiMenu.git
cd ChaiMenu
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

### 5. Run the application

```bash
uvicorn main:app --reload
```

The application will run at:

`http://127.0.0.1:8000`

## API Endpoints

Base URL: `http://127.0.0.1:8000`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/menu` | Retrieve all menu items |
| GET | `/menu?category=tea` | Filter items by category |
| GET | `/menu/{item_id}` | Retrieve an item by ID |

### 1. Welcome Endpoint

```http
GET /
```

Example response:

```json
{
  "message": "Welcome to ChaiMenu API!"
}
```

### 2. Get All Menu Items

```http
GET /menu
```

Returns all available menu items.

### 3. Filter Menu by Category

```http
GET /menu?category=tea
```

Returns menu items belonging to the specified category.

Category filtering is case-insensitive.

Example:

```http
GET /menu?category=Tea
```

If no items match the category, the API returns `404 Not Found`.

### 4. Get Menu Item by ID

```http
GET /menu/1
```

Returns the menu item matching the specified ID.

If the ID does not exist:

```json
{
  "detail": "Menu item with id '100' not found"
}
```

## API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Concepts Practiced

- FastAPI application creation.
- GET endpoints.
- Path parameters.
- Query parameters using `Query()`.
- Optional parameters using Python type hints.
- Pydantic models.
- Response model validation.
- HTTPException and status codes.
- List filtering using Python.

## Future Improvements

- Add menu item creation using POST.
- Implement menu item updates using PUT/PATCH.
- Add menu item deletion using DELETE.
- Integrate a database such as SQLite or MySQL.
- Add automated API tests using Pytest.

---

**Author:** Rajesh Boya

**Project:** ChaiMenu – FastAPI Learning Project