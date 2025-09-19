name = input("Enter file name:")
if len(name) < 1:
    handle = open('../sampleFiles/mbox-short.txt')
else:
    try:
        handle = open(name)
    except:
        print("Invalid File Name!!")

hourcount = {}
sortedtup = tuple()
for line in handle: 
    if line.startswith("From "):
        hour = line.split(" ")[6].split(':')[0] # this line finds the from line, splits it  at ' 'to find the time stamp and then splits the time stamp at ': ' to find the hour
        hourcount[hour] = hourcount.get(hour,0) + 1
        #sortedtup= sorted(((hour, count) for hour, count in hourcount.items()))
        sortedtup = sorted(hourcount.items())

for hour, count in sortedtup : print(hour + " " + str(count))
