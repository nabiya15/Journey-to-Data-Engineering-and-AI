import pytest
from src.analyzer import analyze_readings, load_readings, save_summary, load_readings
import tempfile, os
from pathlib import Path

def test_load_readings_valid_file():
    """Should load numeric readings from a sample text file."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp:
        tmp.write("10\n20\n30\n")
        path = tmp.name
    try:
        values = load_readings(path)
        assert values == [10, 20, 30]
    finally:
        os.remove(path)

def test_empty_readings_error():
    """Should raise ValueError when readings list is empty."""
    with pytest.raises(ValueError):
        analyze_readings([])

def test_analyze_readings():
    readings = [72, 74, 71, 73, 70, 75]
    summary = analyze_readings(readings)

    assert summary["total_readings"] == 6
    assert summary["stable_values"] == [74, 73, 75]    # even-indexed using 0-based indexes -> indices 1,3,5
    assert summary["stable_count"] == 3
    assert summary["sum_stable"] == 222
    assert summary["average_stable"] == 74.0    

def test_load_readings_skips_invalid_lines():
    """Should ignore bad entries and only load numeric readings."""
    import tempfile, os
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp:
        tmp.write("10\nabc\n20\n \n-5\n")
        path = tmp.name
    try:
        values = load_readings(path)
        assert values == [10, 20, -5]
    finally:
        os.remove(path)

def test_save_summary_creates_file(tmp_path):
    """Should create a summary file with expected content."""
    summary = {
        "total_readings": 6,
        "stable_count": 3,
        "sum_stable": 222,
        "average_stable": 74.0,
        "stable_values": [74, 73, 75],
    }

    file_path = tmp_path / "sensor_summary.txt"
    save_summary(summary, str(file_path))

    # Check if file exists and has expected content
    text = file_path.read_text()
    assert "Sensor Data Quality Report" in text
    assert "Total Readings: 6" in text
    assert "Stable Readings Count: 3" in text
    assert "Average Stable Reading: 74.0" in text