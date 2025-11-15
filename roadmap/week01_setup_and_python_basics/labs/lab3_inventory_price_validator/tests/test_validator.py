import os, tempfile
import pytest
from pathlib import Path
from src.validator import load_products, analyze_products, save_summary

def test_load_products_valid_file():
    """Should load products correctly from a sample text file"""
    with tempfile.NamedTemporaryFile(mode = "w", delete = False) as tmp:
        tmp.write("Laptop,1200\nHeadphones,150\nCamera,500\n")
        path = tmp.name
    try:
        products = load_products(path)
        assert products == {
            "Laptop": 1200.0,
            "Headphones": 150.0,
            "Camera": 500.0
        }
    finally:
        os.remove(path) # Clean up the temporary file since it's no longer needed and we set delete=False

def test_load_products_invalid_file():
    """Should raise FileNotFoundError for non-existent file"""
    with pytest.raises(FileNotFoundError):
        load_products("non_existent_file.txt")

def test_analyze_price_correctness():
    """Should analyze products correctly"""
    products = {
        "Laptop": 1200.0,
        "Headphones": 150.0,
        "Keyboard": 80.0,
        "Camera": 500.0
    }
    summary = analyze_products(products)
    assert summary == {
        "total_valid_products": 4,
        "total_inventory_value": 1930.0,
        "average_price": 482.5,
        "product_names": list(products.keys())
    }

def test_analyze_products_empty_dict():
    """Should raise ValueError when analyzing empty products dict"""
    with pytest.raises(ValueError):
        analyze_products({})

def test_save_summary_creates_file(tmp_path:Path):
    """Should create a summary file with correct content"""
    summary = {
        "total_valid_products": 3,
        "total_inventory_value": 1850.0,
        "average_price": 616.67,
        "product_names": ["Laptop", "Headphones", "Camera"]
    }
    file_path = tmp_path / "inventory_summary.txt"
    save_summary(summary, str(file_path))
    with open(file_path, 'r') as file:
        content = file.read()
       
        assert "Total Valid Products" in content
        assert "Total Inventory Value" in content
        assert "Average Price" in content
        assert "Product Names" in content
