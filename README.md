<<<<<<< HEAD
# shopify-api-assessment
=======
# Shopify Product Data Prep for ERP

## What This Project Does
This project connects to a Shopify store, pulls all the product data, and saves it into a CSV file that can easily be imported into an ERP system. The goal was to take the JSON data from Shopify and make it simple, structured, and ready to use elsewhere.

## How I Did It
1. **Set Up**
   - Installed Python and necessary libraries (`requests` and `csv`).
   - Created a Shopify development store and generated an Admin API access token.

2. **Fetching Products**
   - Used the Shopify REST API to get product data.
   - Made sure to handle products with multiple variants (like different sizes or colors).

3. **Transforming Data**
   - Picked the important fields: `ID`, `Title`, `SKU`, `Price`, and `Inventory Quantity`.
   - Saved everything into a CSV file called `products.csv`.

## How to Use
Simply run the Python script:

python shopify_products.py

