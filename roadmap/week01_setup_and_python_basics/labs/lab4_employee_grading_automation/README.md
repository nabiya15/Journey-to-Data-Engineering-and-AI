# Lab 4 - Employee Grading Automation

## 1. Scenario

You’re working with the HR analytics team of a mid-sized company.
They collect annual performance review scores for every employee in a CSV file.
Your job is to **automate the grading process**: read the file, validate scores, assign letter grades (A–F), record any errors, and produce a final graded report.

This system will form part of HR’s internal analytics pipeline — the foundation of performance tracking dashboards.

**Grading Logic**
| Grade | Range | Label |
| ----------- | ------- | ------------- |
| Distinction | > 95 | "Distinction" |
| A | 90 – 95 | "A" |
| B | 80 – 89 | "B" |
| C | 70 – 79 | "C" |
| D | 60 – 69 | "D" |
| F | < 60 | "F" |

**Objective**
Design and implement a system that ingests a CSV, reads raw data from the said CSV, cleans, and computes grades based on the data.

| Step | Goal                                                                    |
| ---- | ----------------------------------------------------------------------- |
| 1    | Read raw employee reviews from a CSV file                               |
| 2    | Validate and clean invalid entries (non-numeric, out-of-range, missing) |
| 3    | Assign grades based on score ranges                                     |
| 4    | Log all invalid rows to an error log                                    |
| 5    | Write a clean output file with grades appended                          |
| 6    | Test the logic with `pytest`                                            |

---

## Folder Structure

```text
lab1_3_employee_grading_automation/
├── src/
│   └── grade_calculator.py
├── tests/
│   └── test_grade_calculator.py
├── data/
│   ├── reviews.csv
│   └── graded_reviews.csv
├── logs/
│   └── error_log.txt
├── main.py
└── README.md

```

## Example Input File:

**data/reviews.csv**

```text
EmployeeID,Name,Department,Score
E001,Ali Khan,Engineering,97
E002,Sara Lopez,HR,88
E003,John Doe,Finance,abc
E004,Aisha Patel,Marketing,73
E005,Michael Lee,Engineering,59
E006,Ravi Sharma,Finance,102
E007,Jane Kim,HR,
E008,Noah Park,Design,95
E009,Mina Chen,Marketing,68
E010,Leo Adams,Engineering,85
```

---

## Expected Output File

**1. data/graded_reviews.csv**

```text
EmployeeID,Name,Department,Score,Grade
E001,Ali Khan,Engineering,97,Distinction
E002,Sara Lopez,HR,88,B
E004,Aisha Patel,Marketing,73,C
E005,Michael Lee,Engineering,59,F
E008,Noah Park,Design,95,A
E009,Mina Chen,Marketing,68,D
E010,Leo Adams,Engineering,85,B
```

**2. logs/error_log.txt**

```text
Invalid score for E003 (non-numeric: abc)
Out-of-range score for E006 (102)
Missing score for E007

```

---

## Function Design Requirements

**load_reviews(filepath: str) -> list[dict]**

- Reads CSV into a list of dictionaries.
- Skips header automatically.
- Returns raw data rows for processing.

**assign_grade(score: float) -> str**

- Converts numeric score to grade based on the table above.
- Raises ValueError for invalid or out-of-range scores.

**process_reviews(data: list[dict], log_path: str) -> list[dict]**

- Validates each row.
- Uses assign_grade() for valid scores.
- Logs invalid rows to error_log.txt.
- Returns a list of graded rows.

**save_graded_reviews(graded_data: list[dict], output_path: str) -> None**

- Writes clean graded results to graded_reviews.csv.

## Testing Requirements

| Test                                    | Description                                       |
| --------------------------------------- | ------------------------------------------------- |
| `test_assign_grade_ranges`              | Correct grade output for valid boundaries         |
| `test_assign_grade_invalid_values`      | Raises `ValueError` for out-of-range or bad input |
| `test_process_reviews_logs_errors`      | Creates log entries for invalid rows              |
| `test_save_graded_reviews_creates_file` | File exists and has correct headers               |

Use tmp_path and temporary files for clean test runs.

### **Resources**

- [Real Python: Read & Write Files in Python](https://realpython.com/read-write-files-python/)
- [W3Schools: Python CSV Module](https://www.w3schools.com/python/python_csv.asp)
- [pytest Docs: Fixtures & tmp_path](https://docs.pytest.org/en/stable/fixture.html)

---
