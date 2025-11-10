# Journey to Data Engineering and AI

**Author:** Nabiya Maredia  
**Last Updated:** October 2025

---

## 1. Overview

This repository documents a structured, hands-on learning roadmap toward becoming a **Data Engineer and AI-focused technologist**.  
Each week represents a stage in developing real-world engineering skills — from foundational Python programming to production-grade data pipelines and AI integrations.

The roadmap emphasizes **production-style problem solving** rather than academic exercises. Every lab is designed as a realistic scenario requiring modular design, testing, documentation, and reflection.

---

## 2. Learning Philosophy

| Core Principle               | Description                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Production-First Design**  | Each assignment simulates a real-world data or system workflow instead of a classroom exercise.                       |
| **Test-Driven Learning**     | Every lab integrates `pytest`-based unit tests to mirror CI/CD validation practices used in production environments.  |
| **Modular Codebase**         | Code is organized into `/src` and `/tests` directories for scalability, readability, and maintainability.             |
| **Documentation Discipline** | Each folder includes professional `README.md` files and in-code docstrings that follow industry conventions.          |
| **Reflection and Growth**    | Every milestone concludes with written reflections, connecting technical skills to professional engineering behavior. |

---

## 3. Repository Structure

```text
Journey-to-Data-Engineering-and-AI/
│
├── week01_environment_and_python_basics/
│   ├── lab1.1_environment_setup/
│   │   ├── setup_log.txt
│   │   └── README.md
│   ├── lab1.2_sensor_data_quality/
│   │   ├── src/
│   │   │   └── analyzer.py
│   │   ├── tests/
│   │   │   └── test_analyzer.py
│   │   ├── data/
│   │   │   └── sample_readings.txt
│   │   ├── main.py
│   │   ├── sensor_summary.txt
│   │   └── README.md
│   └── practice/
│       └── practice_day1.py
│
├── week02_to_be_added/
│
└── README.md
```

| Folder            | Description                                                        |
| ----------------- | ------------------------------------------------------------------ |
| **/src**          | Core logic modules for data processing and transformations.        |
| **/tests**        | `pytest` test cases validating logic and error handling.           |
| **/data**         | Input datasets or simulated samples used for analysis.             |
| **/practice**     | Small exercises and exploratory scripts.                           |
| **/weekXX\_.../** | Each week’s folder contains labs, documentation, and deliverables. |

---

## 4. Testing Framework — Pytest

All labs use **pytest** for automated validation and regression testing, ensuring every function behaves as expected under different conditions.

**Run tests**

```bash
pytest -v
```

**Example test**

```python
def test_analyze_readings_correctness():
    readings = [72, 74, 71, 73, 70, 75]
    from src.analyzer import analyze_readings
    result = analyze_readings(readings)
    assert result["stable_count"] == 3
    assert result["average_stable"] == 74.0
```

**Test categories**

| Category              | Description                                                               |
| --------------------- | ------------------------------------------------------------------------- |
| **Unit Tests**        | Validate specific functions for correctness and expected output.          |
| **Edge-Case Tests**   | Ensure code handles missing, invalid, or empty input gracefully.          |
| **Integration Tests** | Verify that modular components work correctly when orchestrated together. |

---

## 5. Weekly Learning Flow

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

## 6. Tools and Technologies

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

## 7. Professional Practices

| Area                    | Practice                                        | Purpose                                     |
| ----------------------- | ----------------------------------------------- | ------------------------------------------- |
| **Version Control**     | Consistent, descriptive commits using Git       | Track evolution of the codebase.            |
| **Environment Logging** | `setup_log.txt` for Python and package versions | Ensure reproducibility across systems.      |
| **Automated Testing**   | `pytest`-based validation                       | Catch errors early and enforce reliability. |
| **Code Style**          | PEP 8 + clear docstrings                        | Promote readability and collaboration.      |
| **Documentation**       | README and targeted inline comments             | Maintain clarity and self-containment.      |

---

## 8. Reflective Statement

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
