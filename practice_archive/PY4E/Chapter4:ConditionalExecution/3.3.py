entry = input("Enter a score between 0.0 and 1.0:\t")

try:
    score = float(entry)
except:
    print("Invalid Entry!. Please ender a valid number")
    quit()

if score>=0.1 and score <=1.0:
    if score >=0.9:
        print("A")
    elif score >=0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >=0.6:
        print("D")
    else:
        print("F")
else:
    print("Please ender a valid input between 0.1 and 1.0")

