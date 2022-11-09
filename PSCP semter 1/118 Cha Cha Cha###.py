"""[Recommend] Cha Cha Cha"""
from math import ceil
def cha():
    """[Recommend] Cha Cha Cha"""
    workdays = int(input())
    total = 0
    for _ in range(workdays):
        hours = float(input())
        total += ceil(hours)
    print(total*8720)
cha()
