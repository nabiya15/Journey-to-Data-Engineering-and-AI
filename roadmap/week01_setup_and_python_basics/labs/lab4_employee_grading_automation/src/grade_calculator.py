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
    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            record_count += 1   
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
    with open(f"{errfile_path}_{datetime.now().strftime('%m-%d-%Y_%H:%M:%S')}.txt", "w") as errfile:
        for row in employee_records:            
            try:
                if type(row["Score"]) is not int or type(row["Score"]) is not float:
                    row["Score"] = float(row["Score"])
                    
            except ValueError:
                    errfile.write(f"[ERR] Invalid score format for employee {row['EmployeeID']}: {row['Score']}. Score has to be an integer/float.\n")
                    continue
            
            try:
                if row["Score"]==" ":
                    errfile.write(f"[ERR] Missing score for employee {row['EmployeeID']}. Score cannot be empty.\n")
                    continue
                elif row["Score"]>100 or row['Score']<0:
                    errfile.write(f"[ERR]Invalid score for employee {row['EmployeeID']}: {row['Score']}. Score has to be between 0 and 100.\n")
                    continue

            except ValueError as e:
                raise ValueError(f"Malformed data: {e}")  
            grade = assign_grade(row["Score"])
            processed_records.append({**row, "Grade": grade})
            
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

        
            
    

       

             
   


