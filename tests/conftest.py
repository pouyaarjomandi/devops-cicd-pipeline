import pytest
import app as app_module
from app import app

# وضعیت اولیه محصولات — قبل از هر تست reset میشه
INITIAL_PRODUCTS = [
    {"id": 1, "name": "Wireless Headphones", "price": 59.99, "stock": 120},
    {"id": 2, "name": "USB-C Hub", "price": 34.99, "stock": 85},
    {"id": 3, "name": "Mechanical Keyboard", "price": 89.99, "stock": 45},
    {"id": 4, "name": "Monitor Stand", "price": 29.99, "stock": 200},
    {"id": 5, "name": "Laptop Sleeve", "price": 19.99, "stock": 150},
]

@pytest.fixture(autouse=True)
def reset_products():
    app_module.products.clear()
    app_module.products.extend([p.copy() for p in INITIAL_PRODUCTS])
    yield
    app_module.products.clear()
    app_module.products.extend([p.copy() for p in INITIAL_PRODUCTS])

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
