############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
from db.models import Product

# Populate the databse if it is empty
if not Product.objects.exists():
    products = [
        {"upc": "111111111111", "name": "Milk", "price": 2.99},
        {"upc": "222222222222", "name": "Bread", "price": 1.79},
        {"upc": "333333333333", "name": "Eggs", "price": 3.49},
        {"upc": "444444444444", "name": "Cheese", "price": 5.20},
        {"upc": "555555555555", "name": "Jam", "price": 3.24},
        {"upc": "666666666666", "name": "Chicken", "price": 20.0},
    ]
    for p in products:
        Product.objects.create(**p)
    print("Database populated successfully!\n")

# Cash Register Scanning
while True:
    user_input = input("Enter product UPC (or 'exit' to quit): ").strip()
    if user_input.lower() == "exit":
        print("Exiting Cash Register. Goodbye!")
        break
    try:
        product = Product.objects.get(upc=user_input)
        print(f"Product: {product.name}\tPrice: ${product.price}\n")
    except Product.DoesNotExist:
        print("Product was not found. Please Try again.\n")
