"""3nPlus1"""
def plus(count):
    """3nPlus1"""
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            while num != 1:
                if num %2 == 0:
                    num /= 2
                    count += 1
                else:
                    num *= 3
                    num += 1
                    count += 1
        print(count)
        count = 1
plus(1)
