"""Restaurant"""
def res():
    """Restaurant"""
    current = float(input())
    promoprice = float(input())
    discount = float(input())
    offer = float(input())
    if current + offer >= promoprice:
        paywithoffer = (current+offer)*(100-discount)/100
    else:
        paywithoffer = current+offer
    if current >= promoprice:
        paywithoutoffer = current*(100-discount)/100
    else:
        paywithoutoffer = current
    dif = abs(paywithoffer-paywithoutoffer)
    if paywithoffer < paywithoutoffer:
        print("Yes %.3f"%dif)
    elif paywithoffer > paywithoutoffer:
        print("No %.3f"% dif)
    else:
        print("Yes")
res()
