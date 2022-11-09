"""Quadrant"""
def main():
    """Quadrant"""
    valuex = float(input())
    valuey = float(input())
    if valuex > 0 and valuey > 0:
        print("Q1")
    elif valuex < 0 and valuey > 0:
        print("Q2")
    elif valuex < 0 and valuey < 0:
        print("Q3")
    elif valuex > 0 and valuey < 0:
        print("Q4")
    elif valuex == 0 and valuey == 0:
        print("O")
    elif valuex == 0 and valuey != 0:
        print("Y")
    elif valuex != 0 and valuey == 0:
        print("X")
main()
