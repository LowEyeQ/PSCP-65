"""EuclideanDistance2D"""
from math import sqrt
def main():
    """Distance from 2 point"""
    valuex1 = float(input())
    valuey1 = float(input())
    valuex2 = float(input())
    valuey2 = float(input())
    distance = sqrt(((valuex1-valuex2)**2)+((valuey1-valuey2)**2))
    print(distance)
main()
