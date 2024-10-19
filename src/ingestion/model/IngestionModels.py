from pydantic import BaseModel
from datetime import date

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
    email: str

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

class Store(BaseModel):
    id: str
    name: str
    parent_store: str

class User(BaseModel):
    id: str
    name: str