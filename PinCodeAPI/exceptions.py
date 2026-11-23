
from fastapi import Request
from fastapi.responses import JSONResponse


# Custom exception for missing pincodes
class NoPincodeFoundException(Exception):
    def __init__(self, pincode: str):
        self.pincode = pincode


# Custom exception for invalid pincodes
class InvalidPincodeException(Exception):
    def __init__(self, pincode: str):
        self.pincode = pincode


# Handler for missing pincodes
class NoPincodeFoundExceptionHandler:

    @staticmethod
    async def handle(
        request: Request,
        exc: NoPincodeFoundException
    ):
        return JSONResponse(
            status_code=404,
            content={
                "message": (
                    f"No information found for pincode "
                    f"{exc.pincode}."
                )
            }
        )


# Handler for invalid pincodes
class InvalidPincodeExceptionHandler:

    @staticmethod
    async def handle(
        request: Request,
        exc: InvalidPincodeException
    ):
        return JSONResponse(
            status_code=400,
            content={
                "message": (
                    f"Invalid pincode format for "
                    f"{exc.pincode}."
                )
            }
        )
