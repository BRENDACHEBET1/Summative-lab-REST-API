# Inventory Management REST API

A simple Flask REST API for managing inventory items. The project also includes a Command Line Interface (CLI) that interacts with the API and integrates with the OpenFoodFacts API to enrich product information.

## Features

- View all inventory items
- Add new products
- Update product quantity and price
- Delete products
- Search products using the OpenFoodFacts API
- Enrich inventory items with product details from OpenFoodFacts
- Unit tests using pytest

## Technologies Used

- Python
- Flask
- Requests
- Pytest

## Project Structure

```
.
├── app.py
├── cli.py
├── external_api.py
├── tests/
├── Pipfile
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <git@github.com:BRENDACHEBET1/Summative-lab-REST-API.git>
cd Summative-lab-REST-API
```

Install dependencies:

```bash
pipenv install
pipenv shell
```

## Running the Application

Start the Flask server:

```bash
python app.py
```

In another terminal, run the CLI:

```bash
python cli.py
```

## CLI Options

1. View Inventory
2. Add Product
3. Update Product
4. Delete Product
5. Find Product
6. Exit

## Running Tests

Run all tests:

```bash
pytest
```

## External API

This project uses the OpenFoodFacts API to retrieve product information by barcode or product name.

https://world.openfoodfacts.org/

## Author

Brenda Chebet