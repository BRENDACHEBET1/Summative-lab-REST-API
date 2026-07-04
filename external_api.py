import requests

BASE_URL = "https://world.openfoodfacts.org"
HEADERS = {
    "User-Agent": "InventoryApp/1.0"
}

#Fetch product details using a barcode 
def fetch_by_barcode(barcode):
    url = f"{BASE_URL}/api/v2/product/{barcode}.json"

    try:
        
        response = requests.get(
        url,
        headers=HEADERS,
        timeout=10
    )

       
        data = response.json()

        if data.get("status") == 1:
            product = data["product"]

            return {
                "name": product.get("product_name"),
                "brand": product.get("brands"),
                "category": product.get("categories"),
                "image": product.get("image_url")
            }

        return None

    except requests.RequestException as e:
         print("Error:", e)          
         return None

#Fetch by name
def fetch_by_name(name):
    url = f"{BASE_URL}/cgi/search.pl"

    params = {
        "search_terms": name,
        "json": 1,
        "page_size": 1
    }

    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=10)
        print("Status Code:", response.status_code)
        print(response.text)
        response.raise_for_status()

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

        return None

    except Exception as e:
        print("Error:", e)
        return None