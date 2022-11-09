"""SumOfNumber"""
def sumnum():
    """SumOfNumber"""
    totalvalue = int(input())
    total = 0
    while True:
        stop = int(input())
        if stop == -1:
            break
        else:
            total = total + stop
        if total == totalvalue:
            break
    print(total)
sumnum()
