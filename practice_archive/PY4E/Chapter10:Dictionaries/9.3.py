name = input("Enter file name: ")
if len(name) < 1:
    handle = open('../sampleFiles/romeo.txt')
else:
    try:
        handle = open(name)
    except:
        print("Invalid File Name!!")

counts = dict()

#read the file line by line and store the words and their counts in the dictionary
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)+1

# find the biggest word
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count>bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
print(counts)