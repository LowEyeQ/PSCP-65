"""Pringles"""
def pri():
    """Pringles"""
    line1 = input()
    line2 = input()
    line3 = input()
    fin = int(input())
    eat = line2.count(')', 0, fin)
    linenew = " "*fin + line2[fin:]
    left = linenew.count(')')
    print(eat)
    if left > 0:
        print("There are still some left.")
    else:
        print("None.")
    print(line1)
    print(linenew)
    print(line3)
pri()
