"""temperature"""
def main(tem, txt1, txt2):
    """temperature"""
    if txt1 == "C":
        print(celsius(tem, txt2))
    elif txt1 == "F":
        print(farenheit(tem, txt2))
    elif txt1 == "K":
        print(kelvin(tem, txt2))
    else:
        print(rankine(tem, txt2))
def celsius(tem, txt2):
    """celsius"""
    if txt2 == "F":
        return "%.2f"%(tem*9/5+32)
    elif txt2 == "K":
        return "%.2f"%(tem+273.15)
    elif txt2 == "R":
        return "%.2f"%((tem+273.15)*(9/5))
    else:
        return "%.2f"%(tem)
def farenheit(tem, txt2):
    """Farenheit"""
    if txt2 == "C":
        return "%.2f"%((5/9)*(tem-32))
    if txt2 == "K":
        return "%.2f"%((5/9)*(tem-32)+273.15)
    if txt2 == "R":
        return "%.2f"%(tem+459.67)
    else:
        return "%.2f"%(tem)
def kelvin(tem, txt2):
    """Kelvin"""
    if txt2 == "C":
        return "%.2f"%(tem-273.15)
    elif txt2 == "F":
        return "%.2f"%((9/5)*(tem-273.15)+32)
    elif txt2 == "R":
        return "%.2f"%(tem*(9/5))
    else:
        return "%.2f"%(tem)
def rankine(tem, txt2):
    """rankine"""
    if txt2 == "C":
        return "%.2f"%((tem-491.67)*(5/9))
    elif txt2 == "F":
        return "%.2f"%(tem-459.67)
    elif txt2 == "K":
        return "%.2f"%(tem*(5/9))
    else:
        return "%.2f"%(tem)
main(float(input()), input(), input())
