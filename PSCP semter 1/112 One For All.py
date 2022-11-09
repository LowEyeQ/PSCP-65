"""One For All"""
def oneforall():
    """One For All"""
    row = int(input())
    total = ""
    for woo in range(1, row+1):
        name = input()
        if woo == row:
            total += "%s%s%d"%(name, "_", row)
        elif woo % 2 == 0:
            total += "%s%s"%(name, "-"*woo)
        else:
            total += "%s%s"%(name, "*"*woo)
    print(total)
oneforall()
