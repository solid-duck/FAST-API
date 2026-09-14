from fastapi import FastAPI
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str
    description: str | None = Field(None, title="Descrizione dell elemento", max_length=300)
    price: float = Field(..., gt=0, description="Il prezzo deve essere maggiore di zero")
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        item_dict.update({"price_with_tax": item.price + item.tax})
    return item_dict

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result