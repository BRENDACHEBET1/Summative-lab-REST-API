import requests

BASE_URL = "https://world.openfoodfacts.org"

#Fetch product details using a barcode 
def fetch_by_barcode(barcode):
    url = f"{BASE_URL}/api/v2/product/{barcode}.json"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("status") == 1:
            product = data["product"]

            return {
                "name": product.get("product_name"),
                "brand": product.get("brands"),
                "category": product.get("categories"),
                "image": product.get("image_url")
            }

        return {"message": "Product not found"}

    except requests.RequestException:
        return {"message": "Unable to connect to OpenFoodFacts API"}

#Fetch by name
def fetch_by_name(name):
    url = f"{BASE_URL}/cgi/search.pl"

    params = {
        "search_terms": name,
        "json": 1,
        "page_size": 1
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        products = data.get("products")

        if products:
            product = products[0]

            return {
                "name": product.get("product_name"),
                "brand": product.get("brands"),
                "category": product.get("categories"),
                "image": product.get("image_url")
            }

        return {"message": "Product not found"}

    except requests.RequestException:
        return {"message": "Unable to connect to OpenFoodFacts API"}