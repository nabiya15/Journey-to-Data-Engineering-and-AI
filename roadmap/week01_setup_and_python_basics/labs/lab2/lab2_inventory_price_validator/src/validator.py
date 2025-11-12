from typing import List, Dict
from datetime import datetime

def load_products(filepath: str) -> dict:
    """
    - Load product data from a text file (one product per line in format: name,price).
    - Splits each line by comma and converts price to float.
    - Skips bad entries (missing fields, non-numeric prices, negative prices).
    - Returns a dictionary with 'name' and 'price' as key value pair.
    
    Raises:
        FileNotFoundError: if the file does not exist
        ValueError: if no valid products are found
    """
  #  raise NotImplementedError #In user defined base classes, abstract methods should raise this exception when they require derived classes to override the method, or while the class is being developed to indicate that the real implementation still needs to be added.
    products: Dict[str, float] = {}
    with open(filepath, 'r') as file:
        for line in file:
            product = line.strip().split(',')
            # ensure there are exactly two fields before accessing them
            if len(product) != 2:
                print(f"[WARN]Skipping invalid entry: {line.strip()} due to wrong number of fields")
                continue
            name = product[0].strip()
            price_str = product[1].strip()
            if name == "" or price_str == "":
                print(f"[WARN]Skipping invalid entry: {line.strip()} due to empty name or price")
                continue
            try:
                price = float(price_str)
            except ValueError:
                print(f"[WARN]Skipping invalid entry: {line.strip()} due to non-numeric price")
                continue
            # skip negative prices
            if price < 0:
                print(f"[WARN]Skipping invalid entry: {line.strip()} due to negative price: {price}")
                continue
            
            products[name] = price
   
    return products

def analyze_products(products: dict) -> dict:

    """
    - Analyzes the products dictionary to compute:
        - total_products: total number of valid products
        - total inventory_value: sum of all product prices
        - average_price(rounded to 2 decimal places): average price of the products
        -list of product names
    - Returns a summary dictionary with these metrics.
    Raises:
        ValueError: if products is empty
    """
    if not products:
        raise ValueError("No valid products to analyze.")
    total_products = len(products)
    total_inventory_value = sum(products.values())
    average_price = round(total_inventory_value / total_products, 2)
    product_names = list(products.keys())
    summary = {
        "total_valid_products": total_products,
        "total_inventory_value": total_inventory_value,
        "average_price": average_price,
        "product_names": product_names
    }
    print(f"[INFO]Analysis Complete")
    return summary

def save_summary(summary: dict, output_path: str)-> None:
    """
    - Write a clean, timestampedreport of the inventory summary to a text file at the output_path.
    - Summary format:
        ---- Summary Report (YYYY-MM-DD HH:MM:SS) ----
        Total Valid Products: X
        Total Inventory Value: $Y
        Average Price: $Z
        Product Names: name1, name2, name3, ...
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:    
        with open(output_path, 'a') as file:
            file.write(f"---- Summary Report ({timestamp}) ----\n")
            file.write(f"Total Valid Products: {summary['total_valid_products']}\n")
            file.write(f"Total Inventory Value: ${summary['total_inventory_value']}\n")
            file.write(f"Average Price: ${summary['average_price']}\n")
            file.write(f"Product Names: {', '.join(summary['product_names'])}\n\n")
        print(f"[INFO]Summary saved to {output_path}")
    except Exception as e:
        print(f"[ERROR]Failed to save summary: {e}")
        raise
