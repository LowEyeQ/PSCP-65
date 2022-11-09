"""Sequence XXX"""
def seqthirty():
    """Sequence XXX"""
    num1 = int(input())
    num2 = int(input())
    half = num1//2
    for i in range(-half, half+1):
        line = ""
        for j in range(-half, half+1):
            if abs(i) == half or abs(j) == half or abs(i) == abs(j):
                line += "*"
            else:
                line += " "
        print((line+" ")*num2)
seqthirty()
