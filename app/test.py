# from fastapi.testclient import TestClient
# from main import app

# client = TestClient(app)

# def test_get_orders():
#     response = client.get("/orders")
#     assert response.status_code == 200
#     assert len(response.json()) > 0

import requests

def insertData():

    url = "http://127.0.0.1:8000/new-order"
    data = {
        "customer_id": 105,
        "order_date": "2023-11-12",
        "total_amount": 100.00
    }
    response = requests.post(url, json=data)

    print(response.status_code)
    print(response.json())

def updateData():
    url = "http://127.0.0.1:8000/update-order/5"
    data = {
        "customer_id": 555,
        "order_date": "1111-11-11",
        "total_amount": 555.55,
    }

    response = requests.put(url, json=data)

    print(response.status_code)
    print(response.json())

def deleteData():
    url = "http://127.0.0.1:8000/delete-order/105"
    response = requests.delete(url)
    
    print(response.status_code)
    print(response.json())
    
deleteData()
