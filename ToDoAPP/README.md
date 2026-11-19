# FastAPI To-Do Application

A beginner-friendly REST API project built using **Python, FastAPI, Pydantic, and Uvicorn**.

## Features

- **GET** – Retrieve all tasks.
- **GET** – Retrieve a specific task using its ID.
- **POST** – Create a new task.
- **PUT** – Replace an existing task.
- **PATCH** – Partially update an existing task.
- **DELETE** – Delete a task.
- HTTP exception handling for invalid task IDs.
- Pydantic models for request validation.

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## Project Structure

```text
ToDOApp/
├── main.py
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/rajeshboya8/FastAPI.git
cd FastAPI/ToDOApp
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

## Run the Application

```bash
uvicorn main:app --reload
```

## API Documentation

Once the server is running, access the interactive Swagger documentation:

http://127.0.0.1:8000/docs

Alternative API documentation:

http://127.0.0.1:8000/redoc

## Learning Objectives

- Understanding REST API fundamentals.
- Working with HTTP methods.
- Building API endpoints using FastAPI.
- Request validation using Pydantic.
- Handling HTTP exceptions.
- Implementing CRUD operations.

---

**Status:** Learning Project 🚀