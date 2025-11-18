import csv
from datetime import datetime
def load_reviews(file_path:str) -> list[dict]:
    """
    - loads performance reviews from a csv file (one employee record per line)
    - Skips the header
    - Returns employee_record as list of dictonaries with Employee Id, Name, Department, and Score as keys and their corresponding values
    
    Raises the following:
    FileNotFoundError: If the file does not exist
    ValueError: If the file content is malformed

    """
    employee_records:  list[dict] = []
    record_count: int = 0
    with open(file_path, mode='r', newline='') as csvfile: # this line will automatically raise the FileNotFoundError if no file is found( Beauty of with open....)
        reader = csv.DictReader(csvfile)
        #try to convert score to float before appending it to the employee_records list
        for row in reader:
            record_count += 1   
            score = row.get("Score", "").strip()

            if score == "":
                row["Score"] = None
            else:
                try:
                    row["Score"]=float(score)
                except:
                    row["Score"]=score
            employee_records.append(row)

    print(f"[INFO] Loaded {record_count} records from {file_path}")
    return employee_records
    #raise NotImplementedError("Function 'load_reviews' is not yet implemented.")

def assign_grade(score:float)->str:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

def process_reviews(employee_records: list[dict], errfile_path:str) -> list[dict]:
    processed_records = []
    errors = []
    for row in employee_records:
        score = row.get("Score")
        # Case 1 : Missing Score
        if score is None:
            errors.append(f"[ERR] Missing score for employee {row.get('EmployeeID')}.")
            continue
        # Case 2: non-numeric score
        if isinstance(score, str):
            errors.append(f"[ERR] Non-numeric score for employee {row.get('EmployeeID')}:{score}.")
            continue
        # Case 3: Numeric but out of range score
        if(score < 0 or score > 100):
            errors.append(f"[ERR] Invalid score for employee {row.get('EmployeeID')}:{score}. Score must be between 0-100")
            continue 

        # Valid Score -> assign grade
        grade = assign_grade(score)
        processed_records.append({**row, "Grade":grade})
    #only write to error file IF error exists
    if errors:
        timestamp = datetime.now().strftime("%m-%d-%Y_%H:%M:%S")
        error_file = f"{errfile_path}_{timestamp}.txt"
        with open(error_file, "w") as f:
            for e in errors:
                f.write(e+"\n")

    return processed_records


def save_processed_reviews(processed_records: list[dict], output_file_path: str) -> None:

    record_count : int = 0
    with open(output_file_path, mode='w', newline='') as csvfile:
        fieldnames = list(processed_records[0].keys()) if processed_records else []
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
       
        for record in processed_records:
            record_count += 1
            writer.writerow(record)
    print(f"[INFO] Saved {record_count} records to {output_file_path}")
           
    


             
   


