import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from unittest.mock import patch
from external_api import fetch_by_barcode, fetch_by_name

from unittest.mock import patch
from external_api import fetch_by_barcode, fetch_by_name


@patch("external_api.requests.get")
def test_fetch_by_barcode(mock_get):

    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Nutella",
            "brands": "Ferrero",
            "categories": "Chocolate",
            "image_url": "image.jpg"
        }
    }

    product = fetch_by_barcode("3017620422003")

    assert product["name"] == "Nutella"
    assert product["brand"] == "Ferrero"


@patch("external_api.requests.get")
def test_barcode_product_not_found(mock_get):

    mock_get.return_value.json.return_value = {
        "status": 0
    }

    product = fetch_by_barcode("111111")

    assert product is None


@patch("external_api.requests.get")
def test_fetch_by_name(mock_get):

    mock_get.return_value.json.return_value = {
        "products": [
            {
                "product_name": "Nutella",
                "brands": "Ferrero",
                "categories": "Chocolate",
                "image_url": "image.jpg"
            }
        ]
    }

    product = fetch_by_name("Nutella")

    assert product["name"] == "Nutella"
    assert product["brand"] == "Ferrero"


@patch("external_api.requests.get")
def test_name_product_not_found(mock_get):

    mock_get.return_value.json.return_value = {
        "products": []
    }

    product = fetch_by_name("Unknown Product")

    assert product is None