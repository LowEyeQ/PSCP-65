"""Divide3Or5"""
def div(num):
    """Divide3Or5"""
    sums = 0
    for iii in range(1, int(num+1)):
        if iii%3 == 0 or iii % 5 == 0:
            sums += iii
    print(sums)
div(float(input()))
