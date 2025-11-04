name = input("Enter file name: ")
if len(name) < 1:
    handle = open('../sampleFiles/romeo.txt')
else:
    try:
        handle = open(name)
    except:
        print("Invalid File Name!!")
#fname = "romeo.txt"

lst = list()

for line in handle:
    nline = line.rstrip()
    nline = nline.split()
    for word in nline:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
