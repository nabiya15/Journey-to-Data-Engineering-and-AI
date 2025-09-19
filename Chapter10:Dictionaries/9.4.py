name = input("Enter file name:")
if len(name) < 1:
    handle = open('../sampleFiles/mbox-short.txt')
else:
    try:
        handle = open(name)
    except:
        print("Invalid File Name!!")

counts = dict()

for line in handle:
    if line.startswith('From '):
        linearr = line.split(' ')
        email = linearr[1]
        counts[email] = counts.get(email, 0) + 1
    
# find the person with most emails
mostemails = None
mostcounts = None

for email, count in counts.items():
    if mostemails is None or count > mostcounts:
        mostemails = email
        mostcounts = count
print(mostemails, mostcounts)