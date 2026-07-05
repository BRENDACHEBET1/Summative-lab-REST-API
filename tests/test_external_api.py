from unittest.mock import patch
from external_api import fetch_by_barcode


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
def test_product_not_found(mock_get):

    mock_get.return_value.json.return_value = {
        "status": 0
    }

    product = fetch_by_barcode("111111")

    assert product is None