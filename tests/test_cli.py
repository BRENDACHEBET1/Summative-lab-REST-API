from unittest.mock import patch
import requests


@patch("requests.get")
def test_list_products(mock_get):

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = []

    response = requests.get("http://127.0.0.1:5000/inventory")

    assert response.status_code == 200


@patch("requests.post")
def test_add_product(mock_post):

    mock_post.return_value.status_code = 201

    response = requests.post(
        "http://127.0.0.1:5000/inventory",
        json={
            "name": "Milk",
            "quantity": 20,
            "price": 150
        }
    )

    assert response.status_code == 201


@patch("requests.delete")
def test_delete_product(mock_delete):

    mock_delete.return_value.status_code = 200

    response = requests.delete(
        "http://127.0.0.1:5000/inventory/1"
    )

    assert response.status_code == 200