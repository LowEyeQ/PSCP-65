"""Shorten"""
def short():
    """Shorten"""
    num = int(input())
    result = ""
    while num != -1:
        num1 = int(input())
        if num == -1:
            break
        elif num + 1 == num1:
            firstnum = num
            prevnum = num1
            while num + 1 == prevnum:
                num = prevnum
                prevnum = int(input())
            result += ("%d-%d" %(firstnum, num))
            num = prevnum
        else:
            result += ("%d" %num)
            num = num1
        if num != -1:
            result += ", "
    print(result)
short()
