# Lab 1.1 — Environment Setup and Version Logging

**Scenario:**  
You have recently joined a data engineering team responsible for maintaining production ETL pipelines.  
Before you can contribute, your team lead requires that your development environment be **reproducible, auditable, and version-logged**.  
This ensures that all engineers across the team run identical environments — minimizing “it works on my machine” issues in production.

Your task is to **automate the setup validation** of your local Python environment and generate a `setup_log.txt` file that documents key version information.

---

## Question

Design and implement a Python script named `setup_environment.py` that performs the following tasks:

1. **Version Verification:**

   - Retrieve and display the following version details:
     - Python interpreter
     - pip package manager
     - Operating system
     - Virtual environment status (if any)

2. **Package Snapshot:**

   - Retrieve and list the versions of commonly used data engineering libraries:
     - `pandas`, `numpy`, `pytest`, and `requests`
     - If any are missing, handle the exception gracefully and record `"Not Installed"`.

3. **Environment Log Generation:**

   - Write all collected details into a text file named `setup_log.txt`
   - The file must be timestamped and formatted for readability.
   - Include both console output and file output confirmation messages.

4. **Error Handling & Output Validation:**
   - Ensure the script runs without breaking even if certain packages are unavailable.
   - Provide clear log messages in both the console and text file.

---

## Example Output

**Console Output:**

ruby
Copy code

**File Output (`setup_log.txt`):**
Setup log initialized at 2025-11-10 16:24:55.504078

## | Index | Package/Platform |Version |

| 1 | python | Python 3.13.3 |

---

## Submission Checklist

- ✅ `setup_log.py` executes without error
- ✅ `setup_log.txt` created in project folder
- ✅ Code includes docstrings and clear console logs
- ✅ Output verified manually

---

**Next:** Proceed to `lab1.2_sensor_data_quality/README.md`
