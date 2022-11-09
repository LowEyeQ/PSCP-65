"""Circular II"""
import math
def circle():
    """Circular II"""
    line1 = float(input())
    line2 = float(input())
    line3 = float(input())
    line4 = float(input())
    line5 = float(input())
    line6 = float(input())
    distance = math.sqrt(((line1-line4)**2) + ((line2-line5)**2))
    if line3+line6 > distance:
        print("Yes")
    else:
        print("No")
circle()
