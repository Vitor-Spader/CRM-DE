from typing import Union
from datetime import date

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


class Order(BaseModel):
    id: str
    customer_id: str
    date: date
    value : float
    is_canceled: bool
    status: str
    seller_id: str
    store_id: str

class Customer(BaseModel):
    id: str
    name: str
    description: str
    mobile_phone: str
    phone: str

class OrderItem(BaseModel):
    id: str
    order_id: str
    product_id: str
    value: float

class Product(BaseModel):
    id: str
    name: str
    description: str
    group: str

class Stores(BaseModel):
    id: str
    name: str
    parent_store: str

class User(BaseModel):
    id: str
    name: str


@app.post("/Order")
def recv_order(order_data: list[Order]):
    return order_data

@app.post("/Customer")
def recv_order(customer_data: list[Customer]):
    return customer_data

@app.post("/OrderItem")
def recv_order(order_item_data: list[OrderItem]):
    return order_item_data

@app.post("/Product")
def recv_order(product_data: list[Product]):
    return product_data

@app.post("/User")
def recv_order(user_data: list[User]):
    return user_data