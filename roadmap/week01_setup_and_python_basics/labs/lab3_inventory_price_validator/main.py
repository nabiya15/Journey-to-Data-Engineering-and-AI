from src.validator import load_products, analyze_products, save_summary

print("[INFO]Starting Inventory Price Validator...")
input_file = 'data/products.txt'
data = load_products(input_file)
summary = analyze_products(data)
save_summary(summary, input_file, 'inventory_summary.txt')
