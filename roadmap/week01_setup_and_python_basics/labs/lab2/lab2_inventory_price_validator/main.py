from src.validator import load_products, analyze_products, save_summary

print("[INFO]Starting Inventory Price Validator...")
data = load_products('data/products.txt')
summary = analyze_products(data)
save_summary(summary, 'inventory_summary.txt')
