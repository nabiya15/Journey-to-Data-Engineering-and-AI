# Journey to Data Engineering and AI

**Author:** Nabiya Maredia  
**Last Updated:** October 2025

---

## 1. Project Overview

This repository documents a structured, hands-on learning roadmap toward becoming a **Data Engineer and AI-focused technologist**.

Each week represents a stage in developing real-world engineering skills — from foundational Python programming to production-grade data pipelines and AI integrations.

The repository is organized around weekly labs and hands-on projects, each simulating real-world data engineering scenarios rather than academic exercises.

The roadmap emphasizes **production-style problem solving** rather than academic exercises. Every lab is designed as a realistic scenario requiring modular design, testing, documentation, and reflection.

**Key Philosophy:**
Production-first design with test-driven learning, modular code organization, and professional documentation standards.

| Core Principle               | Description                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Production-First Design**  | Each assignment simulates a real-world data or system workflow instead of a classroom exercise.                       |
| **Test-Driven Learning**     | Every lab integrates `pytest`-based unit tests to mirror CI/CD validation practices used in production environments.  |
| **Modular Codebase**         | Code is organized into `/src` and `/tests` directories for scalability, readability, and maintainability.             |
| **Documentation Discipline** | Each folder includes professional `README.md` files and in-code docstrings that follow industry conventions.          |
| **Reflection and Growth**    | Every milestone concludes with written reflections, connecting technical skills to professional engineering behavior. |

---

## 2. Repository Architecture

### Directory Structure

- **`/roadmap/week01_setup_and_python_basics/labs/`** — Core learning labs containing the primary work

  - Each lab follows: `/src` (core logic), `/tests` (pytest validation), `/data` (sample datasets)
  - `main.py` — Entry point orchestrating the lab workflow
  - `README.md` — Lab specification and learning objectives

- **`/practice_archive/`** — Exploratory Python exercises from other sources like "Python for Everybody" or other sources.

  - PY4E is organized by chapter (Dictionaries, Tuples, Regex, Network Programming, etc.)
  - Quick scripts for concept exploration—not production code

- **`/roadmap/nm_de_env/`** — Python virtual environment (Python 3.13)

  - Location: `roadmap/nm_de_env/bin/python`
  - Packages: numpy, pandas, pytest, requests (see pyvenv.cfg for exact config)

- **`/docs/`** — Reference documentation. Contains a documentation of topics that might need future reference.

  - `cli_cmds.md` — Command-line utilities reference
  - `python_libraries/typing.md` — Python typing patterns

---

## 3. Critical Developer Workflows

### Testing Framework — Pytest

All labs use **pytest** for automated validation and regression testing, ensuring every function behaves as expected under different conditions.

**Run tests**

```bash
# Run all tests from lab root directory
pytest -v

# Run specific test file
pytest tests/test_grade_calculator.py -v

# Run with coverage (if coverage installed)
pytest --cov=src
```

**Test categories**

| Category              | Description                                                               |
| --------------------- | ------------------------------------------------------------------------- |
| **Unit Tests**        | Validate specific functions for correctness and expected output.          |
| **Edge-Case Tests**   | Ensure code handles missing, invalid, or empty input gracefully.          |
| **Integration Tests** | Verify that modular components work correctly when orchestrated together. |

### Environment Activation

Use the committed virtual environment at `roadmap/nm_de_env/`:

```bash
source roadmap/nm_de_env/bin/activate  # macOS/Linux
# OR
roadmap/nm_de_env/Scripts/activate     # Windows
```

Verify activation by checking Python executable path matches the venv location.

For example, in my case it is:
**(nm_de_env) nabiyamaredia@macmini Journey-to-Data-Engineering-and-AI %**

### Adding Dependencies

Install packages within the activated environment:

```bash
pip install <package_name>
```

This updates the venv's `site-packages/` directory, which is version-controlled.

---

## 4. Project-Specific Patterns & Conventions

### Modular Code Organization

Every lab follows this pattern:

```
lab_name/
├── src/
│   ├── __init__.py
│   ├── module_name.py      # Core logic with docstrings
│   └── utilities.py        # Shared helpers
├── tests/
│   ├── __init__.py
│   └── test_module_name.py # Pytest test cases
├── data/
│   ├── sample_data.txt     # Test fixtures
│   └── actual_data.txt     # Real datasets
├── logs/
│   └── execution_logs.txt  # Runtime output (gitignored)
├── main.py                 # Orchestration entry point
└── README.md               # Lab specification
```

**Key imports pattern:**

```python
from src.module_name import function_name  # From tests, import from src/
import subprocess  # For system diagnostics (see setup_log.py)
import re          # For text parsing (common in network/regex labs)
```

### Docstring & Documentation Standards

Use professional docstrings following the project's standard:

```python
def calculate_metric(data: list) -> dict:
    """
    Calculate metrics on sensor/employee data.

    Args:
        data: List of numeric readings or scores

    Returns:
        dict with keys: 'average', 'stable_count', 'grade'

    Raises:
        ValueError: If data is empty or contains non-numeric values
    """
    pass
```

Lab READMEs should include:

- Learning objectives aligned to the weekly roadmap
- Scenario description (why this is a real problem)
- Acceptance criteria for completion
- How to run tests and validate output

### File I/O & Data Handling

Common pattern from setup_log.py and regex labs:

```python
# Reading files
with open(log_file, "w") as file:
    file.write(f"Header at {datetime.datetime.now()}\n")
    # Process and write

# Text extraction with regex (see Chapter12:Regex)
import re
numbers = re.findall('[0-9]+', line)  # Extract numbers from strings
```

### Error Handling & Validation

Use try-except blocks for system operations, validate input early:

```python
try:
    version_output = subprocess.run([cmd], capture_output=True, text=True)
    if version_output.returncode == 0:
        # process successful output
    else:
        # handle error output
except FileNotFoundError:
    version = "Not Installed"
```

---

## 5. Integration Points & External Dependencies

### Core Libraries

- **pytest** — Testing framework (all labs)
- **pandas** — Data manipulation (future labs in Phase 2)
- **numpy** — Numerical computing (installed, used in analysis)
- **requests** — HTTP requests (network programming labs)
- **datetime** — Timestamps and logging (setup_log.py pattern)
- **subprocess** — System command execution (diagnostics, dependency checks)
- **re** — Regular expressions (text parsing, network labs)

### Python Version & Requirements

- **Python 3.13.3** (specified in pyvenv.cfg)
- Virtual environment: `/roadmap/nm_de_env/`
- All packages installed within venv (isolated from system Python)

### Network & File Access

Labs may involve:

- File I/O with absolute/relative paths (relative preferred within labs)
- HTTP requests via `requests` library (future: AWS S3, cloud APIs)

---

## 6. Learning Progression & Lab Sequencing

Labs are structured to build in complexity:

1. **Lab 1** — Environment setup & diagnostics (`setup_log.py`)
2. **Lab 2** — Data validation (inventory, sensor data quality)
3. **Lab 3** — Automation & grading logic (employee grading)
4. **Future labs** — SQL analytics, ETL pipelines, dbt, cloud integration

When creating new labs, follow the same structure and maintain backward compatibility with earlier code patterns. Some labs might have multiple labs to provide incremental learning.
Example: lab2/lab2_inventory_price_validator and lab2/lab2_sensor_data_quality

---

## 7. Weekly Learning Flow

| Phase                     | Focus Area                                       | Key Outcomes                                             |
| ------------------------- | ------------------------------------------------ | -------------------------------------------------------- |
| **Foundation**            | Python fundamentals, environment setup           | Build confidence with syntax, logic, and scripting.      |
| **Modularization**        | Structuring reusable codebases                   | Create clean, maintainable project architectures.        |
| **Data Engineering Core** | Ingestion → Validation → Transformation → Export | Learn to design real-world ETL pipelines.                |
| **Analytics & AI**        | Data preprocessing and model integration         | Prepare and analyze data for AI workflows.               |
| **Capstone Projects**     | Full-scale data pipelines and deployments        | Integrate all skills into end-to-end production systems. |

Each week includes:

- **Scenario:** A realistic business or data problem.
- **Implementation:** Modular coding structure (`/src`, `/tests`, `main.py`).
- **Testing:** Automated validation using `pytest`.
- **Documentation:** Clear README with reflection and key takeaways.

---

## 8. Tools and Technologies

| Category                   | Tools / Frameworks                          |
| -------------------------- | ------------------------------------------- |
| **Programming Language**   | Python 3.11+                                |
| **Testing Framework**      | Pytest                                      |
| **Data Libraries**         | Pandas, NumPy                               |
| **Environment Management** | pip, virtualenv                             |
| **Version Control**        | Git & GitHub                                |
| **Documentation**          | Markdown, Google Docstring Style            |
| **Future Modules**         | SQLAlchemy, Apache Airflow, PySpark, Docker |

---

## 9. Professional Practices

| Area                    | Practice                                        | Purpose                                     |
| ----------------------- | ----------------------------------------------- | ------------------------------------------- |
| **Version Control**     | Consistent, descriptive commits using Git       | Track evolution of the codebase.            |
| **Environment Logging** | `setup_log.txt` for Python and package versions | Ensure reproducibility across systems.      |
| **Automated Testing**   | `pytest`-based validation                       | Catch errors early and enforce reliability. |
| **Code Style**          | PEP 8 + clear docstrings                        | Promote readability and collaboration.      |
| **Documentation**       | README and targeted inline comments             | Maintain clarity and self-containment.      |

---

## 10. Guidance to follow for any new lab

- **Preserve existing structure:** Respect `/src`, `/tests`, `/data` separation when modifying labs
- **Write testable code:** Always provide matching test cases in `/tests` (pytest-compatible)
- **Document your work:** Update READMEs with new patterns; follow existing docstring style
- **Use relative imports:** Within labs, import from `src/` using `from src.module import ...`
- **Validate with tests:** Run `pytest -v` before considering work complete
- **Match the learning philosophy:** Labs should simulate real production problems, not toy examples

## 11. Reflective Statement

This repository is an evolving record of how I am training to **think, document, and operate like a professional data engineer**.

Each function, test, and report is designed with the mindset of real-world reliability — transforming conceptual learning into repeatable engineering practice.

By treating each lab as a production problem, I am developing the habits required to:

- Decompose complex data challenges.
- Design modular, testable systems.
- Communicate intent clearly through documentation and structure.

**End goal:** Build a portfolio of tested, documented, and deployable data-engineering projects that reflect real-world readiness for modern AI-driven workflows.

---

**Repository:** <https://github.com/nabiya15/Journey-to-Data-Engineering-and-AI>  
**Contact:** <m.nabiya@gmail.com>
