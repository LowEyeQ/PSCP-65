"""Century"""
from math import ceil
def cen(value):
    """cen"""
    for _ in range(value):
        year = input()
        if year[:4] == "A.D.":
            year = int(year[5:])
        elif year[:4] == "B.E.":
            year = int(year[5:])-543
        if year < 1:
            print("ERROR")
        elif year >= 1 and year <= 100:
            print("1")
        else:
            print(int(ceil(year / 100)))
cen(int(input()))
