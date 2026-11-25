
from datetime import date, datetime

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, func, select

from database import get_session
from models import Order, OrderStatus


router = APIRouter(
    prefix="/stats",
    tags=["Stats"]
)


# GET DAILY ORDER STATISTICS
@router.get("/daily-orders")
def daily_orders(
    target_date: date = Query(
        ...,
        alias="date",
        description="Date in YYYY-MM-DD format"
    ),
    session: Session = Depends(get_session)
):
    start = datetime.combine(
        target_date,
        datetime.min.time()
    )

    end = datetime.combine(
        target_date,
        datetime.max.time()
    )

    summary = {}
    total = 0

    for order_status in OrderStatus:

        count = session.exec(
            select(func.count()).where(
                Order.order_status == order_status,
                Order.created_at.between(start, end)
            )
        ).one()

        summary[order_status.value] = count
        total += count

    summary["total"] = total

    return summary
