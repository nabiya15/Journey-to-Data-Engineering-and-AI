import os
import subprocess
import datetime

print("Setup log initialized")
print("Checking for system requirements...")
headers =[ "Package/Platform", "Version"]
packages = [ "python", "pip", "virtualenv", "os", "git" , "pandas", "numpy", "jupyter", "pytest", "requests"]

log_file = "setup_log.txt"
# print table rows
with open(log_file, "w") as file:
    file.write(f"Setup log initialized at {datetime.datetime.now()}\n\n")
    # Print table headers
    file.write("| Index".ljust(10))
    file.write("| ")
    for col in headers:
        file.write(col.ljust(45))
        file.write("|")
    file.write("\n")
    file.write("-" * 105 + "\n")    
        # Checking for os version, python interpreter, pip mananger, and virtual environment    
    for i , row in enumerate(packages):
        file.write("| " + str(i+1).ljust(8)) # writes index
        file.write("| " + row.ljust(45)) # writes package/platform name
        try: # gets version information
            if row == "os":
                version = os.name + " - " + os.uname().sysname + " " + os.uname().release
            elif row == "virtualenv":
                version = (os.environ['VIRTUAL_ENV'])   if 'VIRTUAL_ENV' in os.environ else "Not Activated"
            elif row == "python" or row == "pip" or row == "git":
                version_output = subprocess.run([row, "--version"], capture_output=True, text=True)
                version = version_output.stdout.strip() if version_output.stdout else version_output.stderr.strip()
            else:
                version_output = subprocess.run(["pip", "show", row], capture_output=True, text=True)
                if version_output.returncode == 0:
                    for line in version_output.stdout.splitlines():
                        if line.startswith("Version:"):
                            version = line.split(":", 1)[1].strip()
                            break
                else:
                    version = "Not Installed"
        except FileNotFoundError:
            version = "Not Installed"
        file.write("| " + version.ljust(44)) # writes version information

        file.write("|"+"\n") 
        file.write("-" * 105 + "\n") 
    file.write(f"Table data successfully written to {log_file}")   
print(f"Setup log written to {log_file}")
