from src.analyzer import load_readings, analyze_readings, save_summary

if __name__ == "__main__":
    print("[INFO] Starting Sensor Data Quality Analyzer...")
    readings = load_readings("data/sample_readings.txt")
    summary = analyze_readings(readings)
    save_summary(summary, "sensor_summary_1.txt")
    print("[INFO] Processing complete.")
