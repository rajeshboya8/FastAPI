
from fastapi import FastAPI, Query, HTTPException
from data import menu_items
from models import MenuItem, MenuResponse

app = FastAPI(
    title="ChaiMenu",
    description="A simple API for managing a menu of items",
)


@app.get("/")
def read_root():
    return {"message": "Welcome to ChaiMenu API!"}


@app.get("/menu", response_model=MenuResponse)
def get_menu(
    category: str | None = Query(
        default=None,
        description="Filter menu items by category"
    )
):
    if category:
        filtered_items = [
            item for item in menu_items
            if item["category"].lower() == category.lower()
        ]
    else:
        filtered_items = menu_items

    if not filtered_items:
        raise HTTPException(
            status_code=404,
            detail=f"No menu items found for category '{category}'"
        )

    return MenuResponse(
        count=len(filtered_items),
        items=filtered_items
    )


@app.get("/menu/{item_id}", response_model=MenuItem)
def get_menu_item(item_id: int):
    for item in menu_items:
        if item["id"] == item_id:
            return item

    raise HTTPException(
        status_code=404,
        detail=f"Menu item with id '{item_id}' not found"
    )
