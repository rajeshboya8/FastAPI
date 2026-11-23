# Pincode API – Indian PIN Code Information API

A REST API built using **Python and FastAPI** to retrieve information about Indian PIN codes, including city, district, and state details.

The project demonstrates REST API development, Pydantic request and response validation, custom exception handling, bulk requests, and dynamic route parameters.

## Features

- Retrieve information using a 6-digit PIN code.
- Get city information by PIN code.
- Get district information by PIN code.
- Get state information by PIN code.
- Retrieve complete location information.
- Support bulk PIN code lookup (up to 20 PIN codes).
- Custom exception handling for invalid and unavailable PIN codes.
- Pydantic request and response models.
- Interactive API documentation using Swagger UI.

## Tech Stack

- **Python**
- **FastAPI**
- **Pydantic**
- **Uvicorn**

## Project Structure

```text
PinCodeAPI/
│
├── main.py          # FastAPI application and endpoints
├── models.py        # Pydantic request/response models
├── exceptions.py    # Custom exceptions and handlers
├── data.py          # Sample PIN code database
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/rajeshboya8/FastAPI.git
cd FastAPI/PinCodeAPI
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
| GET | `/pincode/{pincode}` | Get complete PIN code information |
| POST | `/pincode/bulk` | Retrieve multiple PIN code details |
| GET | `/pincode/{pincode}/city` | Get city |
| GET | `/pincode/{pincode}/district` | Get district |
| GET | `/pincode/{pincode}/state` | Get state |
| GET | `/pincode/{pincode}/location` | Get complete location |

### 1. Welcome Endpoint

```http
GET /
```

Example response:

```json
{
  "message": "Welcome to pincode API"
}
```

### 2. Get Complete PIN Code Information

```http
GET /pincode/515801
```

Example response:

```json
{
  "pincode": "515801",
  "city": "GUntakal",
  "District": "Anantapur",
  "State": "Andhra Pradesh"
}
```

### 3. Get City by PIN Code

```http
GET /pincode/515801/city
```

Example response:

```json
{
  "city": "GUntakal"
}
```

### 4. Get District by PIN Code

```http
GET /pincode/515801/district
```

Example response:

```json
{
  "district": "Anantapur"
}
```

### 5. Get State by PIN Code

```http
GET /pincode/515801/state
```

Example response:

```json
{
  "state": "Andhra Pradesh"
}
```

### 6. Get Complete Location

```http
GET /pincode/515801/location
```

Example response:

```json
{
  "city": "GUntakal",
  "district": "Anantapur",
  "state": "Andhra Pradesh"
}
```

### 7. Bulk PIN Code Lookup

```http
POST /pincode/bulk
```

Request body:

```json
{
  "pincodes": [
    "515801",
    "500001",
    "600001"
  ]
}
```

Example response:

```json
{
  "status": "success",
  "found": 3,
  "not_found": 0,
  "results": [
    {
      "pincode": "515801",
      "city": "GUntakal",
      "District": "Anantapur",
      "State": "Andhra Pradesh"
    }
  ],
  "missing": []
}
```

The API supports up to 20 PIN codes in a single request.

## Custom Exception Handling

The project implements custom exceptions to handle invalid and unavailable PIN codes.

| Exception | HTTP Status | Description |
|---|---|---|
| InvalidPincodeException | 400 | PIN code must contain exactly 6 digits |
| NoPincodeFoundException | 404 | PIN code does not exist in the local dataset |

Example invalid PIN code response:

```json
{
  "message": "Invalid pincode format for 123."
}
```

Example PIN code not found response:

```json
{
  "message": "No information found for pincode 999999."
}
```

## Concepts Practiced

- FastAPI application development.
- GET and POST endpoints.
- Path parameters.
- Request body validation.
- Pydantic BaseModel.
- Field validators.
- Response models.
- Custom exception classes.
- Custom exception handlers.
- JSONResponse.
- Bulk data processing.
- HTTP status codes.
- Python dictionaries and list operations.

## Future Improvements

- Integrate a real Indian PIN code database or external API.
- Add database integration using SQLite or MySQL.
- Improve bulk request validation.
- Add automated API testing using Pytest.
- Add caching for frequently requested PIN codes.
- Implement pagination for larger datasets.

---

**Note:** This project currently uses a predefined in-memory sample dataset. It is intended for learning and API development, not as a complete or authoritative Indian PIN code directory.

**Author:** Rajesh Boya

**Project:** Pincode API – FastAPI Learning Project