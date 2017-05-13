# Assignment 3.1
hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
pay = (float(hrs) * float(rate))
if hrs > 40 :
    otimedelta = (((float(hrs) - 40) * float(rate)) * .5)
    totalpay = float(pay) + float(otimedelta)
    print totalpay
else :
    print pay
    
