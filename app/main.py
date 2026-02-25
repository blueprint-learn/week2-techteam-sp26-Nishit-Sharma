from fastapi import FastAPI, HTTPException
from .model import User, Product

app = FastAPI()


db_users = {}
db_products = {}


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/users")
def read_users():
    # TODO: return all users from the database
    return list(db_users.values())


@app.post("/user", status_code=201)
def create_user(payload: User):
    db_users[payload.id] = payload
    return payload


@app.put("/user")
def update_user(payload: User):
    if payload.id not in db_users:
        raise HTTPException(status_code=404, detail="User not found")
    db_users[payload.id] = payload
    return payload


@app.get("/user")
def get_all_users_prefix(prefix: str):
    # TODO: return all users from the database that match the given name prefix
    return [user for user in db_users.values() if user.name.startswith(prefix)]


@app.delete("/user")
def delete_user(id: int):
    if id not in db_users:
        raise HTTPException(status_code=404, detail="User not found")
    del db_users[id]
    return {"message": "User deleted"}


@app.get("/products")
def read_products():
    # TODO: return all products from the database
    return list(db_products.values())


@app.post("/product", status_code=201)
def create_product(payload: Product):
    db_products[payload.id] = payload
    return payload


@app.put("/product")
def update_product(payload: Product):
    if payload.id not in db_products:
        raise HTTPException(status_code=404, detail="Product not found")
    db_products[payload.id] = payload
    return payload


@app.delete("/product")
def delete_product(id: int):
    if id not in db_products:
        raise HTTPException(status_code=404, detail="Product not found")
    del db_products[id]
    return {"message": "Product deleted"}
