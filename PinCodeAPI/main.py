
from fastapi import FastAPI, HTTPException, status

from data import pincode_db

from models import (
    PincodeRequest,
    PincodeResponse,
    BulkPincodeRequest,
    BulkPincodeResponse
)

from exceptions import (
    NoPincodeFoundException,
    InvalidPincodeException,
    NoPincodeFoundExceptionHandler,
    InvalidPincodeExceptionHandler
)


# Initialize FastAPI
app = FastAPI(
    title="Pincode API",
    description="API to get information about Indian pincodes.",
    version="1.0.0"
)


# Register custom exception handlers
app.add_exception_handler(
    NoPincodeFoundException,
    NoPincodeFoundExceptionHandler.handle
)

app.add_exception_handler(
    InvalidPincodeException,
    InvalidPincodeExceptionHandler.handle
)


# Reusable function to validate and find a pincode
def find_pincode(pincode: str):

    if not pincode.isdigit() or len(pincode) != 6:
        raise InvalidPincodeException(pincode)

    if pincode not in pincode_db:
        raise NoPincodeFoundException(pincode)

    return pincode_db[pincode]


# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to Pincode API"
    }


# Get complete information using GET
@app.get(
    "/pincode/{pincode}",
    response_model=PincodeResponse
)
def get_pincode_info(pincode: str):

    return find_pincode(pincode)


# Get information using POST request body
@app.post(
    "/pincode/lookup",
    response_model=PincodeResponse
)
def lookup_pincode(request: PincodeRequest):

    return find_pincode(request.pincode)


# Get multiple pincodes
@app.post(
    "/pincode/bulk",
    response_model=BulkPincodeResponse,
    status_code=status.HTTP_200_OK
)
def get_bulk_pincode_info(request: BulkPincodeRequest):

    found = 0
    not_found = 0

    results = []
    missing = []

    for pincode in request.pincodes:

        if pincode in pincode_db:
            found += 1
            results.append(pincode_db[pincode])

        else:
            not_found += 1
            missing.append(pincode)

    return {
        "status": "success",
        "found": found,
        "not_found": not_found,
        "results": results,
        "missing": missing
    }


# Get city
@app.get("/pincode/{pincode}/city")
def get_city_by_pincode(pincode: str):

    data = find_pincode(pincode)

    return {
        "city": data["city"]
    }


# Get district
@app.get("/pincode/{pincode}/district")
def get_district_by_pincode(pincode: str):

    data = find_pincode(pincode)

    return {
        "district": data["district"]
    }


# Get state
@app.get("/pincode/{pincode}/state")
def get_state_by_pincode(pincode: str):

    data = find_pincode(pincode)

    return {
        "state": data["state"]
    }


# Get complete location
@app.get("/pincode/{pincode}/location")
def get_location_by_pincode(pincode: str):

    data = find_pincode(pincode)

    return {
        "pincode": data["pincode"],
        "city": data["city"],
        "district": data["district"],
        "state": data["state"]
    }
