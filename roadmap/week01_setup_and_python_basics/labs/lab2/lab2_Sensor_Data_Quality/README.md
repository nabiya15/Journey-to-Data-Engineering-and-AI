# Lab 1.2 — Sensor Data Quality Check

**Objective:**  
Design and implement a Python-based data quality analyzer that simulates how IoT sensor readings are validated and summarized in a production data pipeline.

---

## 1. Scenario

You are part of a **smart infrastructure analytics** team responsible for processing IoT temperature data from roadside sensors.  
Each sensor logs readings every 10 seconds, producing a local file before transmission to a cloud-based data warehouse.

Due to hardware calibration cycles:

- Odd-indexed readings (1st, 3rd, 5th, etc.) are unstable.
- Even-indexed readings represent stable, validated data.

Your task is to build a **Sensor Data Quality Analyzer** — a mini pipeline that:

1. Reads sensor readings from a text file.
2. Filters and analyzes the stable readings.
3. Generates a human-readable summary report.
4. Validates results using automated `pytest` tests.

---

## 2. Learning Outcomes

| Category           | Concept                                | Outcome                                          |
| ------------------ | -------------------------------------- | ------------------------------------------------ |
| **File I/O**       | Read and write structured data         | Develop familiarity with external data ingestion |
| **Modular Design** | Functions and reusable logic           | Improve maintainability and clarity              |
| **Testing**        | Unit testing with `pytest`             | Build reliability and confidence in code         |
| **Error Handling** | Graceful exception management          | Prevent common runtime issues                    |
| **Documentation**  | Inline docstrings and Markdown reports | Strengthen communication and reproducibility     |

---

## 3. Folder Structure

```text
lab1.2_sensor_data_quality/
│
├── src/
│   └── analyzer.py
├── tests/
│   └── test_analyzer.py
├── data/
│   └── sample_readings.txt
├── main.py
├── sensor_summary.txt
└── README.md

| Folder/File                  | Description                                            |
| ---------------------------- | ------------------------------------------------------ |
| **src/analyzer.py**          | Core logic for reading, analyzing, and exporting data. |
| **tests/test_analyzer.py**   | Automated unit tests using `pytest`.                   |
| **data/sample_readings.txt** | Input file simulating IoT sensor logs.                 |
| **main.py**                  | Orchestrates pipeline execution.                       |
| **sensor_summary.txt**       | Output summary report generated after processing.      |
```

## 4. Implementation Plan

| Step  | Task                    | Function / File      | Expected Output                  |
| ----- | ----------------------- | -------------------- | -------------------------------- |
| **1** | Load readings from file | `load_readings()`    | List of valid numeric readings   |
| **2** | Analyze stable readings | `analyze_readings()` | Dictionary with metrics summary  |
| **3** | Save summary report     | `save_summary()`     | Appended `sensor_summary.txt`    |
| **4** | Orchestrate full flow   | `main.py`            | Console + file output            |
| **5** | Validate with tests     | `pytest -v`          | All test cases pass successfully |

5. Testing Overview

Run automated validation using pytest:
pytest -v

Example test case:
def test_analyze_readings_correctness():
readings = [72, 74, 71, 73, 70, 75]
from src.analyzer import analyze_readings
summary = analyze_readings(readings)
assert summary["stable_count"] == 3
assert summary["average_stable"] == 74.0

| Test Case                           | Description                 | Expected Result           |
| ----------------------------------- | --------------------------- | ------------------------- |
| `test_load_readings_valid_file`     | Reads integers correctly    | Returns list of ints      |
| `test_analyze_readings_correctness` | Verifies calculations       | Dict with correct metrics |
| `test_empty_readings_error`         | Handles empty data          | Raises `ValueError`       |
| `test_invalid_input_handling`       | Ignores non-numeric entries | Skips with warning        |

## 6. Example Output

### Console

[INFO] Processing 6 readings...
[INFO] Stable readings extracted: [74, 73, 75]
[INFO] Total stable readings: 3 | Average stable temperature: 74.0
[SUCCESS] Data quality report written to sensor_summary.txt

### File(sensor_summary.txt):

Sensor Data Quality Report — 2025-10-05 16:10:22

Total Readings: 6
Stable Readings Count: 3
Sum of Stable Readings: 222
Average Stable Reading: 74.0
Stable Values: [74, 73, 75]

## 7. Reflection

| Aspect                  | Learning Insight                                            |
| ----------------------- | ----------------------------------------------------------- |
| **Technical**           | Practiced modular Python design and reusable functions.     |
| **Testing**             | Learned to apply pytest for logic verification.             |
| **Error Handling**      | Implemented basic exception control for data quality.       |
| **Engineering Mindset** | Understood the value of validation layers in ETL pipelines. |

Next: Proceed to Week 02 — expanding from file-based input to structured data ingestion (CSV and JSON).
