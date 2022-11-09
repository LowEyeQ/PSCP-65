"""Circular I"""
import math
def main():
    """Circular I"""
    line1 = float(input())
    line2 = float(input())
    line3 = float(input())
    line4 = float(input())
    line5 = float(input())
    distance = math.sqrt(((line1-line4)**2) + ((line2-line5)**2))
    if distance <= line3:
        print("Yes")
    else:
        print("No")
main()
