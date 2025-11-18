import pytest
from src.grade_calculator import process_reviews

# testing logic for process_reviews
'''
Defining it precisely since it is the most important function of this lab

# Contract:
Input: 
    - list of employee dicts
    - errfile_path(string)
Output:
    -list of valid  and graded scores
Side-Effect:
    - error_log file, write error messages to this file
    - skips invalid records
    - adds the Grade field

# Designing the tests in plain english:
Test 1: Valid scores pass though:
    Input: 
        - A valid record with score = 85.0
        - error_file_path

    Expect:
        - Record appears in output
        - no error file generated

Test 2: Score is None -> Skip record + log error
    Input: Score = None
    Expected:
        - record is NOT in output
        - error file contains “missing score”

Test 3: Score is a non-numeric string -> Skip record + log error
    Input: Score = "abc"
    Expected:
        - record is skipped
        - error message includes “non-numeric score”

TEST 4: Score < 0 → skip record + log error
    Input: Score = -5
    Expected:
        - record skipped
        - error file contains the correct message

TEST 5: Score > 100 → skip record + log error
    Input: Score = 101
    Expected:
        - skipped
        - error logged 

TEST 6: Multiple records (mixed valid + invalid)
    Input: 5 records:
        - 3 valid
        - 2 invalid
    Expected:
        - output list length = 3
        - error file contains 2 error messages  

TEST 7: Error file is created with timestamped name
    Expected:
        - a file matching the pattern errpath_MM-DD-YYYY_HH:MM:SS.txt is created  

TEST 8: Correct grades assigned for valid rows
This ensures process_reviews really calls assign_grade.
Example record:
    Score = 95 → Grade A
    Score = 70 → Grade C

TEST 9: process_reviews returns a list of dictionaries
Just a sanity test.

'''

#test 1: Valid Score passes
    # This test ensures:
        # The function returns valid results
        # The grading works
        # No errors are incorrectly logged
        # The output is stable and predictable
    
def test_process_reviews_valid_score_passes(tmp_path):
    # A valid employee record
    records = [{
        "EmployeeID" : "1",
        "Name": "Jane Doe",
        "Department": "Engineering",
        "Score":85.0
    }]
     # Path prefix for the error file
    err_path = tmp_path/"errors"

    # run the function
    processed = process_reviews(records, str(err_path))

    # Assertions
    # 1. Should return exactly one processed record
    assert len(processed) == 1
    record = processed[0]
    # 2. The grade should be correctly assigned
    assert record["Grade"] == "B"
    # 3. All original fields should still exist
    assert record["EmployeeID"] == "1"
    assert record["Name"] == "Jane Doe"
    assert record["Department"] == "Engineering"
    assert record["Score"] == 85.0
    error_files = list(tmp_path.glob("errors_*.txt"))
    assert error_files == []  # no error file should exist

# test 2: Score is none
def test_process_reviews_missing_score(tmp_path):
    records = [
        {
            "EmployeeID": "1",
            "Name": "John Doe",
            "Department": "Engineering",
            "Score": None
        }
    ]

    err_path = tmp_path / "errors"

    processed = process_reviews(records, str(err_path))

    # 1. Skip invalid record
    assert processed == []

    # 2. An error file should be created
    error_files = list(tmp_path.glob("errors_*.txt"))
    assert len(error_files) == 1

    # 3. Error file should contain the correct error message
    content = error_files[0].read_text()
    assert "Missing score for employee 1" in content

# test 3 : Score is non numeric
def test_process_reviews_non_numeric_score(tmp_path):

    records = [
        {
            "EmployeeID": "2",
            "Name": "Alice",
            "Department": "Marketing",
            "Score": "abc"   # invalid non-numeric score
        }
    ]

    err_path = tmp_path / "errors"

    processed = process_reviews(records, str(err_path))

    # 1. Should skip this record
    assert processed == []

    # 2. An error file should be created
    error_files = list(tmp_path.glob("errors_*.txt"))
    assert len(error_files) == 1

    # 3. The error file should contain the correct message
    content = error_files[0].read_text()
    assert "Non-numeric score for employee 2" in content

# ------------------------------------------------------
# TEST 4: NEGATIVE SCORE → SKIP + LOG
# ------------------------------------------------------
def test_process_reviews_negative_score(tmp_path):
    records = [{
        "EmployeeID": "3",
        "Name": "Bob",
        "Department": "Sales",
        "Score": -5
    }]

    err_path = tmp_path / "errors"
    processed = process_reviews(records, str(err_path))

    assert processed == []
    error_files = list(tmp_path.glob("errors_*.txt"))
    assert len(error_files) == 1

    content = error_files[0].read_text()
    assert "Invalid score for employee 3" in content


# ------------------------------------------------------
# TEST 5: SCORE > 100 → SKIP + LOG
# ------------------------------------------------------
def test_process_reviews_score_over_100(tmp_path):
    records = [{
        "EmployeeID": "4",
        "Name": "Carol",
        "Department": "HR",
        "Score": 150
    }]

    err_path = tmp_path / "errors"
    processed = process_reviews(records, str(err_path))

    assert processed == []
    error_files = list(tmp_path.glob("errors_*.txt"))
    assert len(error_files) == 1

    content = error_files[0].read_text()
    assert "Invalid score for employee 4" in content


# ------------------------------------------------------
# TEST 6: MIXED VALID + INVALID RECORDS
# ------------------------------------------------------
def test_process_reviews_mixed_records(tmp_path):
    records = [
        {"EmployeeID": "1", "Name": "A", "Department": "X", "Score": 90},
        {"EmployeeID": "2", "Name": "B", "Department": "Y", "Score": None},
        {"EmployeeID": "3", "Name": "C", "Department": "Z", "Score": "abc"},
        {"EmployeeID": "4", "Name": "D", "Department": "W", "Score": 75},
    ]

    err_path = tmp_path / "errors"
    processed = process_reviews(records, str(err_path))

    assert len(processed) == 2  # only 90 and 75 are valid

    # Check grades
    assert processed[0]["Grade"] == "A"
    assert processed[1]["Grade"] == "C"

    # Error file must exist
    error_files = list(tmp_path.glob("errors_*.txt"))
    assert len(error_files) == 1

    content = error_files[0].read_text()
    assert "Missing score for employee 2" in content
    assert "Non-numeric score for employee 3" in content


# ------------------------------------------------------
# TEST 7: ERROR FILE NAMING PATTERN
# ------------------------------------------------------
def test_process_reviews_error_file_naming(tmp_path):
    records = [{
        "EmployeeID": "1",
        "Name": "A",
        "Department": "B",
        "Score": None
    }]

    err_path = tmp_path / "errors"
    process_reviews(records, str(err_path))

    error_files = list(tmp_path.glob("errors_*.txt"))
    assert len(error_files) == 1

    filename = error_files[0].name
    assert filename.startswith("errors_")
    assert filename.endswith(".txt")


# ------------------------------------------------------
# TEST 8: CORRECT GRADES FOR MULTIPLE VALID VALUES
# ------------------------------------------------------
def test_process_reviews_assigns_grades_correctly(tmp_path):
    records = [
        {"EmployeeID": "1", "Name": "A", "Department": "X", "Score": 95},
        {"EmployeeID": "2", "Name": "B", "Department": "Y", "Score": 82},
        {"EmployeeID": "3", "Name": "C", "Department": "Z", "Score": 68},
    ]

    err_path = tmp_path / "errors"
    processed = process_reviews(records, str(err_path))

    assert len(processed) == 3
    assert processed[0]["Grade"] == "A"
    assert processed[1]["Grade"] == "B"
    assert processed[2]["Grade"] == "D"


# ------------------------------------------------------
# TEST 9: ENSURE RETURN TYPE IS LIST OF DICTS
# ------------------------------------------------------
def test_process_reviews_returns_list_of_dicts(tmp_path):
    records = [{
        "EmployeeID": "1",
        "Name": "A",
        "Department": "B",
        "Score": 90
    }]

    err_path = tmp_path / "errors"
    processed = process_reviews(records, str(err_path))

    assert isinstance(processed, list)
    assert isinstance(processed[0], dict)


