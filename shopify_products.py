import requests

ACCESS_TOKEN = "SHOPIFY_ACCESS_TOKEN"
STORE_NAME = "noku-8067"

url = f"https://{STORE_NAME}.myshopify.com/admin/api/2023-07/products.json"

headers = {
    "X-Shopify-Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Products retrieved successfully!")
    for product in data["products"]:
        print({
            "id": product["id"],
            "title": product["title"],
            "sku": product["variants"][0]["sku"],
            "price": product["variants"][0]["price"],
            "inventory_quantity": product["variants"][0]["inventory_quantity"]
        })
else:
    print("❌ Error:", response.status_code, response.text)


import requests
import csv

ACCESS_TOKEN = "SHOPIFY_ACCESS_TOKEN"
STORE_NAME = "noku-8067"

url = f"https://{STORE_NAME}.myshopify.com/admin/api/2023-07/products.json"

headers = {
    "X-Shopify-Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    products = []

    for product in data["products"]:
        products.append({
            "id": product["id"],
            "title": product["title"],
            "sku": product["variants"][0]["sku"],
            "price": product["variants"][0]["price"],
            "inventory_quantity": product["variants"][0]["inventory_quantity"]
        })

    #Save to CSV
    with open("products.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "sku", "price", "inventory_quantity"])
        writer.writeheader()
        writer.writerows(products)

    print("Products saved to products.csv successfully!")

else:
    print("❌ Error:", response.status_code, response.text)
