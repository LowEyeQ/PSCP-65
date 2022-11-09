"""Binary"""
def bia(txt):
    """Binary"""
    total = []
    if txt == 0:
        print(txt)
    while txt > 0:
        total.append(str(txt%2))
        txt = txt//2
    total.reverse()
    print(*total, sep="")
bia(int(input()))
