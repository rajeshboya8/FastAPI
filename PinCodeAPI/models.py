
from pydantic import BaseModel, Field, field_validator


# Request model for a single pincode
class PincodeRequest(BaseModel):
    pincode: str

    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value):
        if not value.isdigit() or len(value) != 6:
            raise ValueError(
                "Pincode must contain exactly 6 digits"
            )
        return value


# Response model for a single pincode
class PincodeResponse(BaseModel):
    pincode: str
    city: str
    district: str
    state: str


# Request model for multiple pincodes
class BulkPincodeRequest(BaseModel):
    pincodes: list[str] = Field(
        ...,
        min_length=1,
        max_length=20
    )

    @field_validator("pincodes")
    @classmethod
    def validate_pincodes(cls, values):
        for pincode in values:
            if not pincode.isdigit() or len(pincode) != 6:
                raise ValueError(
                    f"Invalid pincode: {pincode}. "
                    "Pincode must contain exactly 6 digits."
                )
        return values


# Response model for bulk lookup
class BulkPincodeResponse(BaseModel):
    status: str
    found: int
    not_found: int
    results: list[PincodeResponse]
    missing: list[str]
