from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"messaggio": "Ciao! Questa è la mia pagina principale"}

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item