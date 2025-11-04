import re
name = input("Enter file name to be analyzed:")
# code either takes the name of the file input by the user. To analyze the sample data just enter 's' when prompted for input or 'a' to analyze actual data
if name.startswith('s'): handle = open('sampleData.txt')
else: handle = open('actualData.txt')

total = 0 
numlist = []
for line in handle:
    line = line.rstrip()
    numfound =  re.findall('[0-9]+', line)
    if numfound:
        numlist= numlist + numfound
    else: continue

total = sum(int(item) for item in numlist)

print('Total = ', total)