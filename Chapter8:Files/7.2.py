# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
sasc= 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count+1
    spos = line.find(' ')
    nline = float(line[spos:].strip())
    sasc = sasc + nline

print("Average spam confidence:",sasc/count)