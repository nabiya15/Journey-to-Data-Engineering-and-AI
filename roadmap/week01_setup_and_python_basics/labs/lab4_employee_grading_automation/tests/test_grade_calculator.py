from pathlib import Path
import pytest, tempfile
from src.grade_calculator import load_reviews

def test_load_reviews_file_not_found():
# test to check if a valid file is loaded
    """Should raise FileNotFoundError if the file does not exist"""
    with pytest.raises(FileNotFoundError):
        load_reviews("non_existent_file.csv")

def test_load_reviews_empty_file():
    # test to check if an empty file is handled correctly
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmpfile:
        tmpfile_path = tmpfile.name
    # The file is empty, so load_reviews should return an empty list
    result = load_reviews(tmpfile_path)
    assert result == [] 

def test_load_reviews_valid_file():
    """
    Tests if load_reviews correctly parses a valid CSV file and returns the expected list of dictionaries.
    """
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmpfile:
        tmpfile.write("EmployeeID,Name,Department,Score\n")
        tmpfile.write("1,John Doe,Engineering,85\n")
        tmpfile.write("2,Jane Smith,Marketing,90\n")
        tmpfile.write("3,Bob Johnson,Sales,78\n")
        tmpfile_path = tmpfile.name

    expected_result = [
        {"EmployeeID": "1", "Name": "John Doe", "Department": "Engineering", "Score": 85},
        {"EmployeeID": "2", "Name": "Jane Smith", "Department": "Marketing", "Score": 90},
        {"EmployeeID": "3", "Name": "Bob Johnson", "Department": "Sales", "Score": 78},
    ]

    result = load_reviews(tmpfile_path)
    assert result == expected_result

def test_assign_grade():{
    
}


