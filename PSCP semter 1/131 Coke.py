"""COKE"""
def main(aaa, bbb, ccc, ddd):
    """COke"""
    if ddd == 0:
        print(0)
    elif bbb == 0:
        print(int(aaa*ddd))
    else:
        ddd -= 1
        num_set1, num_set2 = ddd // bbb, ddd % bbb
        price_per_set = ccc + (aaa*(bbb-1))
        print("%d"%(aaa + price_per_set*num_set1 + num_set2*aaa))
main(float(input()), int(input()), float(input()), float(input()))
