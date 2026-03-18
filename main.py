from fastapi import FastAPI

app = FastAPI(title="p-000 API")


@app.get("/")
def root():
    return {"message": "Hello from p-000"}


@app.get("/items")
def list_items():
    return {"items": ["item-1", "item-2", "item-3"]}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}
