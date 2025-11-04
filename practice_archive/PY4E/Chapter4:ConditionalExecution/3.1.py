hours = float(input("Enter the number of hours worked:"))
rate = float(input("Enter the rate per hour:"))

if hours > 40:
    extrahours = hours - 40
    pay  = (40*rate)+ (extrahours * (rate*1.5)) #pay = base pay + overtime pay
else:
    pay = hours * rate
print("Your pay is $",pay)