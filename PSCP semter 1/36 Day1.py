"""Day1"""
def main():
    """Day1"""
    calen = float(input())
    if calen%4 != 0:
        print("No")
    elif calen%4 == 0 and calen%100 != 0:
        print("Yes")
    elif calen%4 == 0 and calen%100 == 0 and calen%400 == 0:
        print("Yes")
    else:
        print("No")
main()
