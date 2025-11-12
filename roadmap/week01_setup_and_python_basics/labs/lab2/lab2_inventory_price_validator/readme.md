# Lab 1.2.2 — Inventory Price Validator

**Objective:**  
Design and implement a Python program that cleans, validates, and summarizes the data.

| Step | What to Build                      | Goal                                                                            |
| ---- | ---------------------------------- | ------------------------------------------------------------------------------- |
| 1    | Read a file line by line           | Convert valid lines like `"Laptop,1200"` into a Python dict `{"Laptop": 1200}`  |
| 2    | Skip invalid or incomplete entries | Handle missing or negative prices gracefully                                    |
| 3    | Compute a simple summary           | Return total number of valid products, total inventory value, and average price |
| 4    | Write the summary to a text file   | Include a timestamp and formatted output                                        |
| 5    | Test each part with `pytest`       | Cover success cases and error cases                                             |

## 1.Scenario

You work for a **retail analytics startup** that manages thousands of product price feeds from suppliers.
Each day, they send a plain text file containing product names and prices (comma-separated).
Some suppliers send bad data — missing prices, negative numbers, or typos.

Your task: build an **Inventory Price Validator** - a program that cleans, validates, and summarizes the data.
You’ll create three functions (modular, testable) and test them using pytest.

## 2. Learning Outcomes

| Category           | Concept                                | Outcome                                          |
| ------------------ | -------------------------------------- | ------------------------------------------------ |
| **File I/O**       | Read and write structured data         | Develop familiarity with external data ingestion |
| **Modular Design** | Functions and reusable logic           | Improve maintainability and clarity              |
| **Testing**        | Unit testing with `pytest`             | Build reliability and confidence in code         |
| **Error Handling** | Graceful exception management          | Prevent common runtime issues                    |
| **Documentation**  | Inline docstrings and Markdown reports | Strengthen communication and reproducibility     |

---

## 3. Folder Structure:

```text
lab2_inventory_price_validator/
│
├── src/
│ └── validator.py
├── tests/
│ └── test_validator.py
├── data/
│ └── products.txt
├── main.py/
├── inventory_summary.txt/
└── README.md

| Folder/File                 | Description                                           |
| --------------------------- | ----------------------------------------------------- |
| **src/validator.py**        | Core logic for reading, analyzing, and exporting data |
| **tests/test_validator.py** | Automated unit tests using `pytest`.                  |
| **data/products.txt**       | Input file containing product data                    |
| **main.py**                 | Orchestrates pipeline execution.                      |
| **inventory_summary.txt**   | Output summary report generated after processing.     |
```

## 5.Testing Overview

Run automated validation using pytest:
pytest -v
Must write 3 tests:
| Test | What it checks | Example |
| ----------------------------------- | -------------------------- | ---------------------------------- |
| ✅ `test_load_products_valid_file` | Reads valid file correctly | Uses `tempfile.NamedTemporaryFile` |
| ✅ `test_load_products_invalid_input` | Skips invalid lines | Has non-numeric / negative data |
| ✅ `test_analyze_prices_correctness` | Correct total + average | Validates math logic |

## 6 Example Input

```text
Laptop,1200
Headphones,150
Mouse,not_available
Keyboard,80
Monitor,-200
Camera,500

```

## 7. Expected Output

### Console

[INFO] Processing 6 readings...
[INFO] Valid data extracted: {"Laptop": 1200, "Headphones": 150, "Keyboard": 80, "Camera": 500}
[INFO] Total valid products: 4 | Total Value: 1930 | Average price: 482.5 | Products: Laptop, Headphones, Keyboard, Camera
[SUCCESS] Data quality report written to inventory_summary.txt

### File(inventory_summary.txt):

Inventory Summary Report — 2025-11-15 15:35:00
Valid Products: 4
Total Inventory Value: 1930
Average Price: 482.5
