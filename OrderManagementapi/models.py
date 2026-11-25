
from datetime import datetime
from enum import Enum
from typing import Optional

from sqlmodel import Field, SQLModel


# Available order statuses
class OrderStatus(str, Enum):
    PREPARING = "preparing"
    READY = "ready"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


# Database model for orders
class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    customer_name: str
    customer_phone: str
    delivery_address: str
    item_name: str

    order_status: OrderStatus = Field(
        default=OrderStatus.PREPARING
    )

    created_at: datetime = Field(
        default_factory=datetime.now
    )

    updated_at: datetime = Field(
        default_factory=datetime.now
    )


# Schema for creating an order
class OrderCreate(SQLModel):
    customer_name: str
    customer_phone: str
    delivery_address: str
    item_name: str


# Schema for updating an order
class OrderUpdate(SQLModel):
    customer_name: Optional[str] = None
    customer_phone: Optional[str] = None
    delivery_address: Optional[str] = None
    item_name: Optional[str] = None
    order_status: Optional[OrderStatus] = None


# Database model for order status history
class OrderStatusLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    order_id: int
    previous_status: OrderStatus
    new_status: OrderStatus

    changed_at: datetime = Field(
        default_factory=datetime.now
    )
