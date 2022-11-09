"""Seven"""
def main():
    """Seven"""
    exponent = int(input())
    if exponent%4 == 0:
        total = 1
    elif exponent%4 == 1:
        total = 7
    elif exponent%4 == 2:
        total = 9
    elif exponent%4 == 3:
        total = 3
    print(total)
main()
