"""Kaprekar"""
def kap():
    """Kaprekar"""
    total = 0
    num = input()
    while True:
        total += 1
        num1 = int(num[0])
        num2 = int(num[1])
        num3 = int(num[2])
        num4 = int(num[3])
        check = True
        while check == True:
            check = False
            if num1 > num2:
                num1, num2 = num2, num1
                check = True
            if num2 > num3:
                num2, num3 = num3, num2
                check = True
            if num3 > num4:
                num3, num4 = num4, num3
                check = True
        num = str(num1) + str(num2) + str(num3) +str(num4)
        num = "%04d" % (int(num[::-1]) - int(num))
        if num == "6174":
            break
        else:
            continue
    print(total)
kap()
