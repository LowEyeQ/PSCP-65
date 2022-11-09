"""Parity"""
def par(parity, txt):
    """Parity"""
    num = 0
    for iii in parity:
        if iii == "1":
            num += 1
    if num % 2 == 0 and txt == "Even":
        print("%s%d"%(parity, 0))
    elif num % 2 == 0 and txt == "Odd":
        print("%s%d"%(parity, 1))
    elif num % 2 != 0 and txt == "Even":
        print("%s%d"%(parity, 1))
    elif num % 2 != 0 and txt == "Odd":
        print("%s%d"%(parity, 0))
par(input(), input())
