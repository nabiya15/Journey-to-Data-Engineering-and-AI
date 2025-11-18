from src.grade_calculator import load_reviews, assign_grade
import pytest
# tests for load_reviews()

def test_load_reviews_file_not_found():
# test to check if a valid file is loaded. This function is automatically implemented by python when our load_reviews tries to open the file using "with open...."
    """Should raise FileNotFoundError if the file does not exist
    passes because:
        - inside load_reviews, it tries to open("non_existent.csv")
        - immediately raises FileNotFoundError
        - pytest catches it
        - test passes
        -  There is NOTHING more complicated going on.
    """
    with pytest.raises(FileNotFoundError):
        load_reviews("non_existent_file.csv")

def test_load_reviews_empty_file(tmp_path):
    '''
    This file check contains ONLY the header row.
    Meaning: ZERO data records.
    '''
    reviews_file = tmp_path / "reviews.csv"
    # Only header, no data rows
    reviews_file.write_text("EmployeeID,Name,Department,Score\n")

    result = load_reviews(reviews_file)

    assert result == []

def test_load_reviews_converts_score_to_float(tmp_path):
    reviews_file = tmp_path/"reviews.csv"
    reviews_file.write_text(
        "EmployeeID,Name,Department,Score\n"
        "1,John Doe,Engineering,85\n"
    )
    result = load_reviews(reviews_file)

    assert len(result) == 1
    row =result[0]
    assert row["EmployeeID"] == "1"
    assert row["Name"] == "John Doe"
    assert row["Department"] == "Engineering"
    assert row["Score"] == 85.0  # float, not '85'

def test_load_reviews_blank_score_becomes_none(tmp_path):
    reviews_file = tmp_path / "reviews.csv"
    reviews_file.write_text(
        "EmployeeID,Name,Department,Score\n"
        "1,John Doe,Engineering,\n"
    )

    result = load_reviews(reviews_file)

    assert len(result) == 1
    row = result[0]
    assert row["Score"] is None

def test_load_reviews_non_numeric_score_stays_string(tmp_path):
    reviews_file = tmp_path / "reviews.csv"
    reviews_file.write_text(
        "EmployeeID,Name,Department,Score\n"
        "1,John Doe,Engineering,not_available\n"
    )

    result = load_reviews(reviews_file)

    assert len(result) == 1
    row = result[0]
    assert row["Score"] == "not_available"


# tests for assign_grade()
#
def test_assign_grade_invalid_input():
    with pytest.raises(TypeError):
        assign_grade("hello")

def test_assign_grade_A():
    assert assign_grade(90) == 'A'
    assert assign_grade(95) == 'A'
    assert assign_grade(100) == 'A'

def test_assign_grade_B():
    assert assign_grade(80) == "B"
    assert assign_grade(85) == "B"
    assert assign_grade(89.9) == "B"

def test_assign_grade_C():
    assert assign_grade(70) == "C"
    assert assign_grade(75) == "C"
    assert assign_grade(79.9) == "C"

def test_assign_grade_D():
    assert assign_grade(60) == "D"
    assert assign_grade(65) == "D"
    assert assign_grade(69.9) == "D"

def test_assign_grade_F():
    assert assign_grade(0) == "F"
    assert assign_grade(30) == "F"
    assert assign_grade(59.9) == "F"


