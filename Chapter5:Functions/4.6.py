hours = input("Enter hours: ")
rate = input("Enter rate: ")

try:
    hours = float(hours)
    rate = float(rate)
except:
    print("enter a valid integer input and try again")
    quit()

def computepay(h, r):
    if h > 40:
        overtime = h-40
        pay = (40 * r) + (overtime * (rate *1.5))
    else:
        pay = 40 * r

    return pay
    
print(computepay(hours, rate))
