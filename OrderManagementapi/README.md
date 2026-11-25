# Order Management API – FastAPI Application

A RESTful API built using **Python, FastAPI, SQLModel, and SQLite** to manage customer orders and generate daily order statistics.

The application allows users to create orders, retrieve orders using different filters, track order statuses, and generate daily summaries based on order status.

This project demonstrates database integration, Enum-based status management, query parameters, date filtering, pagination, and SQL aggregation.

## Features

- Create customer orders.
- Retrieve all orders.
- Filter orders by status.
- Filter orders by creation date.
- Support pagination using `skip` and `limit`.
- Generate daily order statistics.
- Track different order statuses.
- Automatically generate order IDs.
- Automatically record creation and update timestamps.
- Store order information using SQLite.
- Organize endpoints using FastAPI APIRouter.
- Manage database sessions using dependency injection.
- Health check endpoint.

## Tech Stack

- Python
- FastAPI
- SQLModel
- SQLite
- Pydantic
- Uvicorn

## Project Structure

```text
OrderManagementAPI/
│
├── main.py                 # Main FastAPI application
├── models.py               # Order and status models
├── database.py             # Database configuration
│
├── routes/
│   ├── __init__.py
│   ├── orders.py            # Order management endpoints
│   └── stats.py             # Order statistics endpoints
│
├── orders.db                # Generated SQLite database
├── requirements.txt
├── .gitignore
└── README.md
```

## Order Statuses

The application supports four order statuses using Python Enum.

| Status | Description |
|---|---|
| preparing | Order is being prepared |
| ready | Order is ready for delivery |
| delivered | Order has been delivered |
| cancelled | Order has been cancelled |

New orders automatically receive the `preparing` status.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd OrderManagementAPI
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

The SQLite database and tables are created automatically when the application starts.

## API Endpoints

Base URL: `http://127.0.0.1:8000`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check API health |
| POST | `/orders/` | Create a new order |
| GET | `/orders/` | Retrieve all orders |
| GET | `/orders/?status=preparing` | Filter orders by status |
| GET | `/orders/?created_date=2026-11-25` | Filter orders by date |
| GET | `/stats/daily-orders?date=2026-11-25` | Generate daily statistics |

## API Usage and Examples

### 1. Health Check

**Endpoint:**

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

### 2. Create a New Order

**Endpoint:**

```http
POST /orders/
```

Request body:

```json
{
  "customer_name": "Rajesh",
  "customer_phone": "9876543210",
  "delivery_address": "Hyderabad, Telangana",
  "item_name": "Masala Chai"
}
```

Response: `201 Created`

```json
{
  "id": 1,
  "customer_name": "Rajesh",
  "customer_phone": "9876543210",
  "delivery_address": "Hyderabad, Telangana",
  "item_name": "Masala Chai",
  "order_status": "preparing",
  "created_at": "2026-11-25T10:30:00",
  "updated_at": "2026-11-25T10:30:00"
}
```

The order ID and timestamps are generated automatically.

### 3. Retrieve All Orders

**Endpoint:**

```http
GET /orders/
```

Returns all orders, with a default pagination limit of 20.

### 4. Filter Orders by Status

**Endpoint:**

```http
GET /orders/?status=preparing
```

Supported values:

- preparing
- ready
- delivered
- cancelled

Example:

```http
GET /orders/?status=delivered
```

### 5. Filter Orders by Creation Date

**Endpoint:**

```http
GET /orders/?created_date=2026-11-25
```

Returns orders created on the specified date.

Date format: `YYYY-MM-DD`

### 6. Pagination

The API supports pagination using `skip` and `limit`.

Example:

```http
GET /orders/?skip=0&limit=5
```

- `skip`: Number of orders to skip.
- `limit`: Maximum number of orders to return.

Filtering and pagination can be combined:

```http
GET /orders/?status=preparing&skip=0&limit=5
```

### 7. Daily Order Statistics

**Endpoint:**

```http
GET /stats/daily-orders?date=2026-11-25
```

Generates a summary of orders created on the specified date, grouped by order status.

Example response:

```json
{
  "preparing": 5,
  "ready": 3,
  "delivered": 10,
  "cancelled": 2,
  "total": 20
}
```

The statistics are calculated dynamically using SQL aggregation.

## Database Design

The application uses SQLite and SQLModel ORM.

### Order Table

| Column | Data Type | Description |
|---|---|---|
| id | Integer | Primary key |
| customer_name | String | Customer name |
| customer_phone | String | Customer phone number |
| delivery_address | String | Delivery address |
| item_name | String | Ordered item |
| order_status | Enum | Current order status |
| created_at | DateTime | Order creation timestamp |
| updated_at | DateTime | Order update timestamp |

### OrderStatusLog Table

| Column | Data Type | Description |
|---|---|---|
| id | Integer | Primary key |
| order_id | Integer | Associated order ID |
| previous_status | Enum | Previous order status |
| new_status | Enum | New order status |
| changed_at | DateTime | Status change timestamp |

The status history model is defined for future order tracking functionality.

## API Documentation

FastAPI automatically generates interactive API documentation.

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Concepts Practiced

- FastAPI application development.
- REST API architecture.
- SQLModel ORM.
- SQLite database integration.
- Database engine and session management.
- Dependency injection using Depends().
- APIRouter and modular routing.
- Python Enum classes.
- Query parameters.
- Date-based filtering.
- Pagination using offset and limit.
- SQL aggregation using func.count().
- Database table creation.
- Application lifespan management.
- Health check endpoints.

## Future Improvements

- Add GET order by ID.
- Implement order status updates.
- Implement order cancellation.
- Add PATCH and DELETE endpoints.
- Maintain order status history using OrderStatusLog.
- Automatically update `updated_at` whenever an order changes.
- Add customer-based order filtering.
- Add automated testing using Pytest.
- Introduce Alembic database migrations.
- Add authentication and authorization.
- Add Docker support.
- Deploy to a cloud platform.

---

**Author:** Rajesh Boya

**Project:** Order Management API – FastAPI Learning Project