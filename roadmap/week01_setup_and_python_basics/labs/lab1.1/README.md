# Data Engineering Roadmap - Assignment 1

### 🗓️ Lab 1.1: Environment Setup & System Check

This marks the first step in my Data Engineering and AI learning journey — a quiet but significant beginning.  
Before diving into code, pipelines, or transformations, I wanted to make sure the foundation was ready.  
This week’s task was to verify my environment setup, confirm that Python is installed globally, and record the system configuration that will carry me through this roadmap.

## ✨ Overview

This repository documents my environment setup for **Week 1** of the Data Engineering Roadmap.  
It includes:

- My globally installed Python version
- The system path to my Python executable
- pip version and installed libraries
- A generated log file (`setup_log.txt`) capturing all these details

The purpose was simple — to ensure that my machine is prepared, stable, and ready for the months of experimentation and learning ahead.

---

## 🧰 Commands Used

I’m currently using a **global Python installation** (not a virtual environment), I used these commands to verify and log my setup.

### Since I am using Mac 🍎:

```bash
where python > setup_log.txt
python --version >> setup_log.txt
pip --version >> setup_log.txt
pip list >> setup_log.txt
```

### Also researched them for Windows 🪟:

```bash
which python3 >setup_log.txt
python3 --version >> setup_log.txt
pip3 --version >> setup_log.txt
pip3 list >> setup_log.txt
```

These simple commands not only display the versions but also redirect the results into a text file, forming a traceable log for future reference.

### 📄 Example Output (setup_log.txt)

/Users/nabiyamaredia/Desktop/Data Engineering/nm_de_env/bin/python
Python 3.13.3
pip 25.3 from /Users/nabiyamaredia/Desktop/Data Engineering/nm_de_env/lib/python3.13/site-packages/pip (python 3.13)
Package Version

---

### 💭 Reflection

This first assignment may look small, but it felt symbolic —
a way of acknowledging that every big data system starts with one working environment, one clean setup, and one line of code that runs successfully.
I learned how to:

- Log command-line outputs into a text file (>, >>)
- Confirm global Python and pip paths
- Keep structured documentation using Markdown
- Begin treating every project, no matter how small, as something worth documenting. Each of these steps is a quiet rehearsal for the more complex documentation I’ll be writing later — for pipelines, ETL projects, and capstones that will shape this roadmap into something tangible.

### 📎 Next Steps

- Create a Github repository and explore Github in connection with VS Code
- Begin working on the first python assignment
