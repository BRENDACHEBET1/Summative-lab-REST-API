import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import app, inventory


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        inventory.clear()
        yield client


def test_get_inventory(client):
    response = client.get("/inventory")

    assert response.status_code == 200
    assert response.get_json() == []


def test_add_product(client):
    response = client.post(
        "/inventory",
        json={
            "name": "Milk",
            "quantity": 20,
            "price": 150
        }
    )

    assert response.status_code == 201
    assert response.get_json()["quantity"] == 20


def test_update_product(client):
    inventory.append({
        "id": 1,
        "name": "Milk",
        "quantity": 20,
        "price": 150
    })

    response = client.patch(
        "/inventory/1",
        json={
            "price": 200
        }
    )

    assert response.status_code == 200
    assert response.get_json()["price"] == 200


def test_delete_product(client):
    inventory.append({
        "id": 1,
        "name": "Milk",
        "quantity": 20,
        "price": 150
    })

    response = client.delete("/inventory/1")

import pytest
from app import app, inventory


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        inventory.clear()
        yield client


def test_get_inventory(client):
    response = client.get("/inventory")

    assert response.status_code == 200
    assert response.get_json() == []


def test_add_product(client):
    response = client.post(
        "/inventory",
        json={
            "name": "Milk",
            "quantity": 20,
            "price": 150
        }
    )

    assert response.status_code == 201
    assert response.get_json()["quantity"] == 20


def test_update_product(client):
    inventory.append({
        "id": 1,
        "name": "Milk",
        "quantity": 20,
        "price": 150
    })

    response = client.patch(
        "/inventory/1",
        json={
            "price": 200
        }
    )

    assert response.status_code == 200
    assert response.get_json()["price"] == 200


def test_delete_product(client):
    inventory.append({
        "id": 1,
        "name": "Milk",
        "quantity": 20,
        "price": 150
    })

    response = client.delete("/inventory/1")

    assert response.status_code == 200