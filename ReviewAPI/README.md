# Review API – FastAPI CRUD Application

A RESTful API built using **Python, FastAPI, SQLModel, and SQLite** to create, retrieve, update, and delete play reviews.

The application also supports filtering reviews by play name, pagination, and calculating average ratings.

This project demonstrates REST API development, database integration, SQLModel ORM, CRUD operations, dependency injection, and request/response validation.

## Features

- Create reviews for plays.
- Retrieve all available reviews.
- Filter reviews by play name.
- Retrieve reviews with pagination.
- Calculate average ratings for a specific play.
- Update existing reviews using PATCH.
- Delete reviews by ID.
- Validate ratings between 1 and 5.
- Automatically generate review IDs.
- Automatically record UTC timestamps.
- Persist review information using SQLite.
- Organize endpoints using FastAPI APIRouter.
- Manage database sessions using dependency injection.

## Tech Stack

- Python
- FastAPI
- SQLModel
- SQLite
- Pydantic
- Uvicorn

## Project Structure

```text
ReviewAPI/
│
├── main.py                 # Main FastAPI application
├── models.py               # Database and Pydantic models
├── database.py             # SQLite engine and session management
│
├── routes/
│   ├── __init__.py
│   └── reviews.py          # Review API endpoints
│
├── reviews.db              # SQLite database (generated automatically)
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd ReviewAPI
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
pip install -r requirements.txt
```

### 5. Start the application

```bash
uvicorn main:app --reload
```

The application runs at:

`http://127.0.0.1:8000`

## API Endpoints

Base URL: `http://127.0.0.1:8000`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| POST | `/reviews/` | Create a review |
| GET | `/reviews/` | Retrieve all reviews |
| GET | `/reviews/?play_name=Hamlet` | Filter reviews |
| GET | `/reviews/average_rating?play_name=Hamlet` | Calculate average rating |
| PATCH | `/reviews/{review_id}` | Update a review |
| DELETE | `/reviews/{review_id}` | Delete a review |

## API Usage and Examples

### 1. Welcome Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Welcome to Review API"
}
```

### 2. Create a Review

```http
POST /reviews/
```

Request body:

```json
{
  "play_name": "Hamlet",
  "reviewer_name": "Rajesh",
  "rating": 5,
  "comment": "Excellent performance and storytelling."
}
```

Response: `201 Created`

```json
{
  "id": 1,
  "play_name": "Hamlet",
  "reviewer_name": "Rajesh",
  "rating": 5,
  "comment": "Excellent performance and storytelling.",
  "created_at": "2026-11-24T10:00:00Z"
}
```

The review ID and timestamp are generated automatically.

### 3. Retrieve All Reviews

```http
GET /reviews/
```

Returns a list of stored reviews.

### 4. Filter Reviews by Play Name

```http
GET /reviews/?play_name=Hamlet
```

Returns reviews associated with the specified play name.

### 5. Pagination

```http
GET /reviews/?skip=0&limit=5
```

- `skip`: Number of records to skip.
- `limit`: Maximum number of records to retrieve.

Filtering and pagination can also be combined:

```http
GET /reviews/?play_name=Hamlet&skip=0&limit=5
```

### 6. Calculate Average Rating

```http
GET /reviews/average_rating?play_name=Hamlet
```

Calculates the average rating of all reviews for the specified play.

Example response:

```json
4.5
```

If no reviews are found, the API returns a `404 Not Found` response.

### 7. Update a Review

```http
PATCH /reviews/1
```

Request body:

```json
{
  "rating": 4,
  "comment": "Good performance."
}
```

Only the provided fields are updated. Other fields remain unchanged.

### 8. Delete a Review

```http
DELETE /reviews/1
```

Deletes the review with ID `1` and returns the deleted review.

If the review does not exist, the API returns `404 Not Found`.

## Database Design

The application uses SQLite with SQLModel ORM.

### Review Table

| Column | Data Type | Description |
|---|---|---|
| id | Integer | Primary key |
| play_name | String | Name of the play |
| reviewer_name | String | Name of the reviewer |
| rating | Integer | Rating between 1 and 5 |
| comment | String | Optional review comment |
| created_at | DateTime | UTC creation timestamp |

The database and table are created automatically when the application starts.

## Validation and Error Handling

- Ratings must be between 1 and 5.
- Review IDs are automatically generated.
- Comments are optional.
- Creation timestamps are automatically generated.
- Pagination parameters are validated.
- Missing reviews return HTTP 404.
- Invalid rating values are rejected through model validation.

## API Documentation

FastAPI automatically generates interactive API documentation.

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Concepts Practiced

- FastAPI application development.
- REST API architecture.
- CRUD operations.
- SQLModel ORM.
- SQLite database integration.
- Database engine and session management.
- Dependency injection using Depends().
- APIRouter and modular routing.
- Pydantic request and response models.
- Path and query parameters.
- Pagination using offset and limit.
- SQL aggregation using func.avg().
- Partial updates using PATCH.
- HTTPException and status codes.
- Automatic timestamp generation.

## Future Improvements

- Add authentication and authorization.
- Add an endpoint to retrieve a review by ID.
- Add sorting by rating and creation date.
- Add search functionality.
- Add automated tests using Pytest.
- Introduce database migrations using Alembic.
- Add Docker support.
- Deploy the API to a cloud platform.

---

**Author:** Rajesh Boya

**Project:** Review API – FastAPI Learning Project