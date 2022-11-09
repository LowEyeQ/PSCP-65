"""diamond"""
def dia():
    """diamond"""
    rows = int(input())
    i = 1
    if rows%2 == 1:
        while i <= rows//2:
            j = rows//2+1
            while j > i:
                print(' ', end='')
                j -= 1
            print('*', end='')
            k = 1
            while k < 2*(i-1):
                print(' ', end='')
                k += 1
            if i == 1:
                print()
            else:
                print('*')
            i += 1
        print("*"*rows)
        i = rows//2
        while i >= 1:
            j = rows//2+1
            while j > i:
                print(' ', end='')
                j -= 1
            print('*', end='')
            k = 2
            while k <= 2 * (i-1):
                print(' ', end='')
                k += 1
            if i == 1:
                print()
            else:
                print('*')
            i -= 1
dia()
