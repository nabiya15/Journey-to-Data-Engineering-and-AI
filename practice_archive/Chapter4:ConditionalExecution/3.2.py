#exercise 3.1 with exception/error handling

hours = input("Enter the number of hours worked:")
rate = input("Enter the rate per hour:")
try:
    fhours = float(hours)
    frate = float(rate)
except:
    print("Invalid Input. Please enter a valid input in form of a number or decimals")
    quit()
if fhours > 40:
    extrahours = fhours - 40
    pay  = (40*frate)+ (extrahours * (frate*1.5)) #pay = base pay + overtime pay
else:
    pay = fhours * frate
print("Your pay is $",pay)