from fastapi import FastAPI
app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}

#@app.get("/items/")
#def read_items():
 #   return {"items": ["item1", "item2", "item3"]}

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {"user_id": user_id, "name": "John Doe"}
#
# @app.get("/items/")
# def get_items(skip: int = 0, limit: int = 10):
#     return {"skip": skip, "limit": limit}

#Get merr te dhana
#Post krijon te dhena(dergon te dhena ne server)
#Put update te dhenat
#Delete fshin

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    return {"item_id": item_id, "item_name": name, "item_price": price}

@app.post("/items/")
def create_item(name: str, price: float):
    return {"item_name": name, "item_price": price}

# DELETE - fshin te dhena
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted successfully"}