from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict
from .authapi import User, get_current_active_user

# Initialize FastAPI
router = APIRouter()

# In-memory database for demonstration purposes
fake_db: Dict[int, dict] = {}


# Define a Pydantic model for your data
class Item(BaseModel):
    name: str
    description: str
    


# Create operation (POST)
@router.post("/items/")
async def create_item(item: Item, current_user: User = Depends(get_current_active_user)):
    item_dict = item.dict()
    item_id = len(fake_db) + 1
    fake_db[item_id] = item_dict
    return {"item_id": item_id, **item_dict}


# Read operation (GET)
@router.get("/items/{item_id}")
async def read_item(item_id: int, current_user: User = Depends(get_current_active_user)):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]


# Update operation (PUT)
@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, current_user: User = Depends(get_current_active_user)):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = item.dict()
    return {"message": "Item updated successfully"}


# Delete operation (DELETE)
@router.delete("/items/{item_id}")
async def delete_item(item_id: int, current_user: User = Depends(get_current_active_user)):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_db[item_id]
    return {"message": "Item deleted successfully"}
