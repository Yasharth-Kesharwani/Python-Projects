import calendar 
try:   
    yy = int(input("Enter the Year(Ex- 2017) : "))
    mm = int(input("Enter the Month(Ex- 10) : "))
    print(calendar.month(yy, mm))
except Exception:
    print("INVALID INPUT !")