from datetime import date

from fastapi import FastAPI
from model.IngestionModels import Order, Customer, OrderItem, Product, User, Store

app = FastAPI()

@app.post("/Order")
def recv_order(order_data: list[Order]):
    return order_data

@app.post("/Customer")
def recv_customer(customer_data: list[Customer]):
    return customer_data

@app.post("/OrderItem")
def recv_order_item(order_item_data: list[OrderItem]):
    return order_item_data

@app.post("/Product")
def recv_product(product_data: list[Product]):
    return product_data

@app.post("/Store")
def recv_store(store_data: list[Store]):
    return store_data

@app.post("/User")
def recv_user(user_data: list[User]):
    return user_data

##########################
#Get Data

@app.get("/Order")
def recv_all_order():
    return {
        "id": "orderId",
        "customer_id": "customerId",
        "date": date.today(),
        "value" : 10.50,
        "is_canceled": False,
        "status": "Closed",
        "seller_id": "sellerId",
        "store_id": "storeId"
    }

@app.get("/Customer")
def recv_all_customer():
    return {
        "id": "customerId",
        "name": "Joao da Silva",
        "description": "",
        "mobile_phone": "+5554999999999",
        "phone": "+555413461346",
        "email": "teste@teste.com"
    }

@app.get("/OrderItem")
def recv_all_order_item():
    return {
        "id": "orderItemId",
        "order_id": "orderId",
        "product_id": "productId",
        "value": 10.50
    }

@app.get("/Product")
def recv_all_product():
    return {
        "id": "productId",
        "name": "Panela de Pressão",
        "description": "Panela de Pressão para ferijão",
        "group": "Panelas"
    }

@app.get("/Store")
def recv_all_store():
    return {
        "id": "storeId",
        "name": "Loja Central",
        "parent_store": ""
    }

@app.get("/User")
def recv_all_user():
    return {
        "id": "sellerId",
        "name": "Joçao Vendedor"
    }