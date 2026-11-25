
from datetime import date, datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, Query, status
from sqlmodel import Session, select

from database import get_session
from models import Order, OrderCreate, OrderStatus


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


# CREATE ORDER
@router.post(
    "/",
    response_model=Order,
    status_code=status.HTTP_201_CREATED
)
def create_order(
    order: OrderCreate,
    session: Session = Depends(get_session)
):
    new_order = Order(**order.model_dump())

    session.add(new_order)
    session.commit()
    session.refresh(new_order)

    return new_order


# GET ALL ORDERS WITH FILTERING AND PAGINATION
@router.get("/", response_model=List[Order])
def list_orders(
    status: Optional[OrderStatus] = Query(None),
    created_date: Optional[date] = Query(
        None,
        description="Filter by YYYY-MM-DD"
    ),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1),
    session: Session = Depends(get_session)
):
    query = select(Order)

    if status:
        query = query.where(
            Order.order_status == status
        )

    if created_date:
        start = datetime.combine(
            created_date,
            datetime.min.time()
        )

        end = datetime.combine(
            created_date,
            datetime.max.time()
        )

        query = query.where(
            Order.created_at.between(start, end)
        )

    query = query.offset(skip).limit(limit)

    return session.exec(query).all()
