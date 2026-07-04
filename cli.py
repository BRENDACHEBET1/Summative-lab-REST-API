import requests

API_BASE = "http://127.0.0.1:5000"

while True:
    print("\n===== Inventory CLI =====")
    print("1. View Inventory")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Find Product")
    print("6. Exit")

    choice = input("Choose an option: ")

    # View Inventory
    if choice == "1":
        response = requests.get(f"{API_BASE}/inventory")

        if response.status_code == 200:
            items = response.json()

            if not items:
                print("Inventory is empty.")
            else:
                for item in items:
                    print(f"ID: {item['id']}")
                    print("-" * 40)
                    print(f"Name: {item['name']}")
                    print(f"Brand: {item.get('brand', 'N/A')}")
                    print(f"Category: {item.get('category', 'N/A').split(',')[0].replace('en:', '')}")
                    print(f"Barcode: {item.get('barcode', 'N/A')}")
                    print(f"Quantity: {item['quantity']}")
                    print(f"Price: {item['price']}")
                    print(f"Source: {item['source']}")
                   
        else:
            print("Error retrieving inventory.")
    # Add Product
    elif choice == "2":
        barcode = input("Barcode (press Enter if unknown): ")
        name = ""

        if not barcode:
            name = input("Product name: ")

        quantity = int(input("Quantity: "))
        price = float(input("Price: "))

        data = {
            "barcode": barcode,
            "name": name,
            "quantity": quantity,
            "price": price
        }

        response = requests.post(f"{API_BASE}/inventory", json=data)
        print(response.json())

    # Update Product
    elif choice == "3":
        item_id = input("Product ID: ")

        data = {}

        quantity = input("New quantity (leave blank to skip): ")
        if quantity:
            data["quantity"] = int(quantity)

        price = input("New price (leave blank to skip): ")
        if price:
            data["price"] = float(price)

        response = requests.patch(
            f"{API_BASE}/inventory/{item_id}",
            json=data
        )

        print(response.json())

    # Delete Product
    elif choice == "4":
        item_id = input("Product ID: ")

        response = requests.delete(f"{API_BASE}/inventory/{item_id}")
        print(response.json())

    # Find Product
    elif choice == "5":
        search = input("Search by (1) Barcode or (2) Name? ")

        if search == "1":
            barcode = input("Barcode: ")
            response = requests.get(
                f"{API_BASE}/search",
                params={"barcode": barcode}
            )

        elif search == "2":
            name = input("Product name: ")
            response = requests.get(
                f"{API_BASE}/search",
                params={"name": name}
            )

        else:
            print("Invalid option.")
            continue

        print(response.status_code)
        print(response.text)

    # Exit
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")