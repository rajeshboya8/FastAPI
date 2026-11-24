
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select, func

from models import Review, ReviewCreate, ReviewRead, ReviewUpdate
from database import get_session


router = APIRouter(
    prefix="/reviews",
    tags=["reviews"]
)


# CREATE REVIEW
@router.post("/", response_model=ReviewRead, status_code=201)
def create_review(
    review: ReviewCreate,
    session: Session = Depends(get_session)
):
    db_review = Review.model_validate(review)

    session.add(db_review)
    session.commit()
    session.refresh(db_review)

    return db_review


# READ ALL REVIEWS
@router.get("/", response_model=list[ReviewRead])
def read_reviews(
    play_name: str | None = Query(
        default=None,
        description="Filter reviews by play name"
    ),
    skip: int = Query(
        default=0,
        ge=0,
        description="Number of items to skip"
    ),
    limit: int = Query(
        default=10,
        ge=1,
        description="Number of items to return"
    ),
    session: Session = Depends(get_session)
):
    query = select(Review)

    if play_name:
        query = query.where(Review.play_name == play_name)

    query = query.offset(skip).limit(limit)

    reviews = session.exec(query).all()

    return reviews


# GET AVERAGE RATING
@router.get("/average_rating", response_model=float)
def get_average_rating(
    play_name: str,
    session: Session = Depends(get_session)
):
    average_rating = session.exec(
        select(func.avg(Review.rating)).where(
            Review.play_name == play_name
        )
    ).one()

    if average_rating is None:
        raise HTTPException(
            status_code=404,
            detail="No reviews found for the specified play."
        )

    return average_rating


# UPDATE REVIEW
@router.patch("/{review_id}", response_model=ReviewRead)
def update_review(
    review_id: int,
    review_update: ReviewUpdate,
    session: Session = Depends(get_session)
):
    db_review = session.get(Review, review_id)

    if not db_review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    update_data = review_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_review, key, value)

    session.add(db_review)
    session.commit()
    session.refresh(db_review)

    return db_review


# DELETE REVIEW
@router.delete("/{review_id}", response_model=ReviewRead)
def delete_review(
    review_id: int,
    session: Session = Depends(get_session)
):
    db_review = session.get(Review, review_id)

    if not db_review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    session.delete(db_review)
    session.commit()

    return db_review
