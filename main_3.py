from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}
    limit: int = Field(10, gt=0)
    offset : int = Field(0, gt=0)
    order_by: str= "created_at"
    tags: list[str] = []

@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query

#@app.get("/items/")
#async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
 #   return results

#oppure 
#async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixedquwey$")] = None]):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results

#oppure una validazione più efficacec con gt, le
#app.get("/items/{item_id}")
#async def read_item(item_id: Annotated[int, Path(titel="ID dell'elemento", gt=0),]):le=1000]):
#    return {"item_id": item_id}