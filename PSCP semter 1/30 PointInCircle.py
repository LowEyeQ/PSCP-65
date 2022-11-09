"""PointInCircle"""
import math
def main():
    """PointInCircle"""
    valuex = float(input())
    valuey = float(input())
    valuer = float(input())
    valuex1 = float(input())
    valuey1 = float(input())
    distance = math.sqrt(((valuex-valuex1)**2)+((valuey-valuey1)**2))
    if distance <= valuer:
        print("True")
    else:
        print("False")
main()
