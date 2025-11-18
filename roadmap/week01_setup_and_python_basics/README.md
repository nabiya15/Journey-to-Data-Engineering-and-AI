# Week 1 Technical Handbook

Foundations of Python, Data Validation, ETL Logic, and Test-Driven Development  
Journey-to-Data-Engineering-and-AI  
Author: Nabiya M.

---

## Table of Contents

1. Introduction
2. Python Environments and Execution Model
3. File I/O and CSV Processing
4. Data Cleaning, Transformation, and Validation Logic
5. Test-Driven Development and Pytest
6. Temporary Files, Directories, and Pattern Matching
7. Project Structure and Modularity
8. Writing and Validating CSV Output
9. Challenges Encountered and Resolutions
10. Reference Tables and Cheat Sheets
11. Recommended AI-Based Practice Resource

---

## 1. Introduction

Week 1 established the foundation for building reliable data engineering workflows.  
The primary objectives were:

- Understand Python’s execution environment (virtual environments, interpreter paths).
- Learn to read and write structured files, especially CSV.
- Design validation logic to detect and handle bad data.
- Implement ETL-style transformations on realistic datasets.
- Structure a small project using `src/`, `tests/`, `data/`, and `output/`.
- Write and run tests with `pytest`.
- Develop the mindset of a production engineer.

---

## 2. Python Environments and Execution Model

**References**

- Python venv module: https://docs.python.org/3/library/venv.html
- Virtual environment primer: https://realpython.com/python-virtual-environments-a-primer/

### 2.1 Purpose of a Virtual Environment

A virtual environment is an isolated Python workspace containing:

- Its own interpreter
- Project-specific dependencies
- Its own `pip` installation
- Isolated `site-packages`

This prevents dependency conflicts across projects.

### 2.2 Conceptual Layout

```
System Python
│
├── nm_de_env/
│    ├── bin/python
│    ├── pytest
│    ├── installed dependencies
│    └── isolated environment
│
└── other environments
```

### 2.3 Activation and Usage

Once activated, the virtual environment becomes the primary execution environment for:

- Running Python scripts
- Running pytest
- Installing dependencies

This ensures reproducibility and isolation.

---

## 3. File I/O and CSV Processing

**References**

- File I/O tutorial: https://docs.python.org/3/tutorial/inputoutput.html
- CSV documentation: https://docs.python.org/3/library/csv.html

### 3.1 Basic File Reading

```python
with open("file.csv", "r", newline="") as f:
    data = f.read()
```

### 3.2 Using csv.DictReader

Transforms rows into dictionaries using headers:

CSV:

```
EmployeeID,Name,Department,Score
1,John Doe,Engineering,85
```

Parsed:

```python
{"EmployeeID": "1", "Name": "John Doe", "Department": "Engineering", "Score": "85"}
```

### 3.3 Type Normalization

Your enhanced loader converts:

- Empty → `None`
- Numeric text → `float`
- Invalid numeric fields → left as strings

```python
score = row.get("Score", "").strip()

if score == "":
    row["Score"] = None
else:
    try:
        row["Score"] = float(score)
    except ValueError:
        row["Score"] = score
```

---

## 4. Data Cleaning, Transformation, and Validation Logic

**References**

- Exception handling: https://realpython.com/python-exceptions/
- ETL overview: https://www.geeksforgeeks.org/etl-extract-transform-load/

### 4.1 ETL Pipeline Structure (Week 1)

```
Extract   → load_reviews()
Validate  → process_reviews()
Transform → assign_grade()
Load      → save_processed_reviews()
```

### 4.2 Final Validation Logic

```python
def process_reviews(employee_records: list[dict], errfile_path:str) -> list[dict]:
    processed_records = []
    errors = []

    for row in employee_records:
        score = row.get("Score")

        # Missing
        if score is None:
            errors.append(f"[ERR] Missing score for employee {row.get('EmployeeID')}.")
            continue

        # Non-numeric
        if isinstance(score, str):
            errors.append(f"[ERR] Non-numeric score for employee {row.get('EmployeeID')}:{score}.")
            continue

        # Out-of-range
        if (score < 0 or score > 100):
            errors.append(
                f"[ERR] Invalid score for employee {row.get('EmployeeID')}:{score}. Score must be between 0 and 100."
            )
            continue

        # Valid
        grade = assign_grade(score)
        processed_records.append({**row, "Grade": grade})

    # Write errors if present
    if errors:
        from datetime import datetime
        timestamp = datetime.now().strftime("%m-%d-%Y_%H:%M:%S")
        error_file = f"{errfile_path}_{timestamp}.txt"
        with open(error_file, "w") as f:
            for e in errors:
                f.write(e + "\n")

    return processed_records
```

### 4.3 Importance of Validation Order and `continue`

The validation order prevents invalid records from being processed:

1. Missing
2. Non-numeric
3. Out-of-range
4. Valid → grade + append

`continue` ensures invalid rows stop immediately and never reach transformation.

---

## 5. Test-Driven Development and Pytest

**References**

- Pytest documentation: https://docs.pytest.org/en/latest/
- Python testing guide: https://realpython.com/python-testing/

### 5.1 Purpose of Testing

Testing was used to:

- Validate assumptions
- Guard against regressions
- Identify flawed logic (e.g., missing `continue`)
- Clarify expected behavior

### 5.2 `pytest.raises`

```python
with pytest.raises(FileNotFoundError):
    load_reviews("missing.csv")
```

This ensures:

- `open()` raises the correct error
- Your function does not mask or mishandle it

### 5.3 `tmp_path` Fixture

Creates isolated directories for each test.

```python
def test_load(tmp_path):
    p = tmp_path / "reviews.csv"
    p.write_text("content")
```

Benefits:

- No risk to real project files
- Each test starts clean
- Easy file manipulation

### 5.4 `glob` Pattern Matching

```python
error_files = list(tmp_path.glob("errors_*.txt"))
```

Used to check:

- No file created for valid data
- Exactly one file for invalid batches

---

## 6. Temporary Files, Directories, and Pattern Matching

### 6.1 When to Use `write_text`

Best for test input generation:

```python
file.write_text("header\nrow1\nrow2\n")
```

### 6.2 When to Use `open() + DictReader`

Best for CSV output validation:

```python
with open(output, newline="") as f:
    rows = list(csv.DictReader(f))
```

### 6.3 Comparison Table

| Purpose              | Method                |
| -------------------- | --------------------- |
| Create input files   | `write_text()`        |
| Validate CSV output  | `open()` + DictReader |
| Read plain-text logs | `read_text()`         |

---

## 7. Project Structure and Modularity

**Reference**: https://packaging.python.org/en/latest/

### 7.1 Adopted Structure

```
lab4_employee_grading_automation/
    src/
        grade_calculator.py
    tests/
        test_grade_calculator.py
        test_process_reviews.py
        test_save_processed_reviews.py
    data/
        reviews.csv
    output/
```

### 7.2 Benefits

- Separation of concerns
- Predictable imports
- Clean test boundaries
- Production-style organization

---

## 8. Writing and Validating CSV Output

**Reference**: https://docs.python.org/3/library/csv.html#csv.DictWriter

### 8.1 Writer Logic

```python
with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(record)
```

### 8.2 Test Strategy

- Validate header
- Validate row count
- Validate field ordering
- Validate numeric values persisted correctly

---

## 9. Challenges Encountered and Resolutions

| Issue                             | Cause                       | Resolution                          |
| --------------------------------- | --------------------------- | ----------------------------------- |
| Confusion about FileNotFoundError | Misunderstood pytest.raises | Learned open() raises automatically |
| Invalid rows being graded         | Missing `continue`          | Added strict control flow           |
| Non-numeric score not caught      | Type normalization gap      | Added `isinstance(score, str)`      |
| Incorrect imports                 | Running pytest in wrong dir | Always run from project root        |
| Error logs created unnecessarily  | File opened prematurely     | Only created logs if errors exist   |

---

## 10. Reference Tables and Cheat Sheets

### 10.1 File I/O Cheat Sheet

| Task                | Pattern               |
| ------------------- | --------------------- |
| Create test CSV     | `write_text()`        |
| Read CSV            | `DictReader`          |
| Write CSV           | `DictWriter`          |
| Validate CSV output | `open() + DictReader` |

### 10.2 Validation Flow Cheat Sheet

```python
if score is None: ...
elif isinstance(score, str): ...
elif score < 0 or score > 100: ...
else: assign_grade(score)
```

### 10.3 Pytest Cheat Sheet

```python
pytest -v
pytest tests/test_file.py::test_case
```

Patterns:

```python
with pytest.raises(Exception):
    fn()

def test(tmp_path):
    p = tmp_path/"file.txt"
    p.write_text("data")
```

---

## 11. Recommended AI-Based Practice Resource

**Codecrafters – Python Track**  
https://codecrafters.io/python

Ideal for strengthening:

- Parsing
- Validation
- Testing
- CLI and automation
- File and network handling

---

_End of Week 1 Technical Handbook_
