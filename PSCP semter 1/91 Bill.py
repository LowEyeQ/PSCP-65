"""bill"""
def bill():
    """ bill """
    food = int(input())
    ser = food*(10/100)
    vat = (food+ser)*(7/100)
    if 1000 >= ser >= 50:
        print("%.2f"%(food+ser+vat))
    elif ser <= 50:
        num = 50
        vat1 = (food+num)*(7/100)
        print("%.2f"%(food+num+vat1))
    elif ser >= 1000:
        num1 = 1000
        vat2 = (food+num1)*(7/100)
        print("%.2f"%(food+num1+vat2))
bill()
