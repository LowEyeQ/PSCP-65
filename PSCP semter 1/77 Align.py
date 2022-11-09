"""Align"""
def align():
    """Align"""
    sizelight = int(input())
    order = input()
    text = input()
    num = len(text)
    num1 = sizelight - num
    num2 = num1//2
    num3 = num1%2
    if order == "left":
        print(text.ljust(sizelight))
    elif order == "center":
        print(" "*(num2+num3) + text + " "*num2)
    elif order == "right":
        print(text.rjust(sizelight))
align()
