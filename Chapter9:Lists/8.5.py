name = input("Enter file name:")
if len(name) < 1:
    handle = open('../sampleFiles/mbox-short.txt')
else:
    try:
        handle = open(name)
    except:
        print("Invalid File Name!!")
count = 0
for line in handle:
    if line == ' ':
        continue
    line = line.rstrip()
    if line.startswith('From '):
        fline = line.split()
        count = count+1
        print(fline[1])
     
print("There were", count, "lines in the file with From as the first word")