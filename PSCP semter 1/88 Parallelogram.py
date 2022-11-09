"""Parallelogram"""
def parall():
    """Parallelogram"""
    var = input()
    varlen = len(var)
    for row in range(varlen):
        for _ in range(varlen-row-1):
            print(" ", end="")
        for col in range(row+1):
            print(var[col], end="")
        print()
    for col in range(varlen-1, 0, -1):
        print(var[-col:])
parall()
