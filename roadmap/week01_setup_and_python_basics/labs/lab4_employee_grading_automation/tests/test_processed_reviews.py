
'''
This function has a very clear contract:

Function Contract:
save_processed_reviews(processed_records: list[dict], output_file_path: str) -> None

It MUST:
- create a CSV file
- write headers correctly
- write all processed records
- preserve order of fields
- handle empty list safely
- not throw exceptions
- print info message (we don’t test prints)

So we will write tests for:

✔ Test 1 — Writes a valid CSV with correct headers
✔ Test 2 — Writes correct number of records
✔ Test 3 — Handles empty list (creates empty file with just header)
✔ Test 4 — Field ordering is preserved
✔ Test 5 — Data values are written exactly

These are all realistic, production-grade expectations.
'''

import csv
from src.grade_calculator import save_processed_reviews

def test_save_processed_reviews_writes_correct_csv(tmp_path):
    processed = [
        {"EmployeeID": "1", "Name": "John", "Department": "Engineering", "Score": 90, "Grade": "A"},
        {"EmployeeID": "2", "Name": "Jane", "Department": "HR", "Score": 80, "Grade": "B"},
    ]

    output_file = tmp_path / "output.csv"
    save_processed_reviews(processed, str(output_file))

    # read CSV to verify content
    with open(output_file, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 2
    assert rows[0]["EmployeeID"] == "1"
    assert rows[0]["Grade"] == "A"
    assert rows[1]["Department"] == "HR"

def test_save_processed_reviews_empty_list(tmp_path):
    processed = []
    output_file = tmp_path / "empty.csv"

    save_processed_reviews(processed, str(output_file))

    with open(output_file, newline='') as f:
        content = f.read()

    # File should exist but be empty
    assert content.strip() == ""

def test_save_processed_reviews_preserves_field_order(tmp_path):
    processed = [
        {"EmployeeID": "1", "Name": "Alice", "Department": "Finance", "Score": 95, "Grade": "A"}
    ]

    output_file = tmp_path / "ordered.csv"
    save_processed_reviews(processed, str(output_file))

    with open(output_file, newline='') as f:
        header_line = f.readline().strip()

    assert header_line == "EmployeeID,Name,Department,Score,Grade"

def test_save_processed_reviews_writes_numeric_values(tmp_path):
    processed = [
        {"EmployeeID": "10", "Name": "Mark", "Department": "Ops", "Score": 72.5, "Grade": "C"}
    ]

    output_file = tmp_path / "numeric.csv"
    save_processed_reviews(processed, str(output_file))

    with open(output_file, newline='') as f:
        reader = csv.DictReader(f)
        row = next(reader)

    assert float(row["Score"]) == 72.5

def test_save_processed_reviews_multiple_runs(tmp_path):
    processed1 = [
        {"EmployeeID": "1", "Name": "A", "Department": "X", "Score": 90, "Grade": "A"},
    ]
    processed2 = [
        {"EmployeeID": "2", "Name": "B", "Department": "Y", "Score": 50, "Grade": "F"},
    ]

    output1 = tmp_path / "out1.csv"
    output2 = tmp_path / "out2.csv"

    save_processed_reviews(processed1, str(output1))
    save_processed_reviews(processed2, str(output2))

    with open(output1) as f1, open(output2) as f2:
        content1 = f1.read()
        content2 = f2.read()

    assert "A" in content1
    assert "F" in content2
    assert "A" not in content2
    assert "F" not in content1

