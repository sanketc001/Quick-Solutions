from fastapi import FastAPI
app = FastAPI()

@app.get("/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}