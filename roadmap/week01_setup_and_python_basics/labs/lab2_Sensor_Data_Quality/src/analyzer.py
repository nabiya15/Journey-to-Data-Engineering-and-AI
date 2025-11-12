import pytest
from typing import List, Dict
from datetime import datetime

def load_readings(filepath: str) -> List[int]:
    """
    Loads numeric readings from a text file (one per line).
    Ignores empty lines or invalid entries gracefully.

    Args:
        filepath (str): Path to the text file.

    Returns:
        List[int]: Clean list of numeric readings.

    Raises:
        FileNotFoundError: If the file path is invalid.
        ValueError: If no valid readings are found.
    """
    readings: List[int] = []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:  # skip blank lines
                    continue
                try:
                    value = int(line)
                    readings.append(value)
                except ValueError:
                    print(f"[WARN] Ignored invalid entry: {line}")
                    continue
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")

    if not readings:
        raise ValueError("No valid numeric readings found.")

    print(f"[INFO] Loaded {len(readings)} valid readings.")
    return readings


def analyze_readings(readings: List[int]) -> Dict:
    """
    Filter even-indexed (stable) readings and compute metrics:
      - total_readings, stable_count, sum_stable, average_stable, stable_values
    Raises:
        ValueError: if readings is empty
    """
    if not readings:
        raise ValueError("Readings list is empty")  
    #pick values at 0 based indices or indices 1,3,5 (the even -numbered readings in real life)
    stable_values = [val for i, val in enumerate(readings) if i%2 ==1]
    total_readings = len(readings)
    stable_count = len(stable_values)
    sum_stable = sum(stable_values)
    average_stable = round(sum_stable / stable_count,1) if stable_count > 0 else 0

    return {
        "total_readings": total_readings,
        "stable_count": stable_count,
        "sum_stable": sum_stable,
        "average_stable": average_stable,
        "stable_values": stable_values
    }

def save_summary(summary: Dict, output_path: str) -> None:
    """
    Append a human-readable summary with a timestamp to output_path.
    """
    raise NotImplementedError


def save_summary(summary: Dict, output_path: str) -> None:
    """
    Writes a human-readable summary of sensor data analysis to a text file.

    Args:
        summary (dict): The computed metrics dictionary.
        output_path (str): Path to output file (e.g., 'sensor_summary.txt').

    Notes:
        - Appends to the file if it already exists.
        - Includes a timestamp for traceability.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(output_path, "a", encoding="utf-8") as f:
            f.write(f"Sensor Data Quality Report — {timestamp}\n\n")
            f.write(f"Total Readings: {summary['total_readings']}\n")
            f.write(f"Stable Readings Count: {summary['stable_count']}\n")
            f.write(f"Sum of Stable Readings: {summary['sum_stable']}\n")
            f.write(f"Average Stable Reading: {summary['average_stable']}\n")
            f.write(f"Stable Values: {summary['stable_values']}\n\n")

        print(f"[SUCCESS] Data quality report written to {output_path}")

    except Exception as e:
        print(f"[ERROR] Failed to write summary: {e}")
        raise
