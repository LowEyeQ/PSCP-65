"""Coupon"""
def cou(price, cou_1, cou_2):
    """Coupon"""
    if price >= float(cou_1[1]):
        sale_1 = price - float(cou_1[0])
    elif price < float(cou_1[1]):
        sale_1 = price
    if price >= float(cou_2[1]):
        sale_2 = ((100 - float(cou_2[0]))/100) * price
    elif price < float(cou_2[1]):
        sale_2 = price
    if sale_1 < sale_2:
        print("%d %.1f"%(1, sale_1))
    elif sale_2 < sale_1:
        print("%d %.1f"%(2, sale_2))
    elif sale_2 == sale_1 and sale_2  != price:
        if float(cou_1[1]) < float(cou_2[1]):
            print("%d %.1f"%(1, sale_1))
        elif float(cou_2[1]) < float(cou_1[1]):
            print("%d %.1f"%(2, sale_2))
        if float(cou_1[1]) == float(cou_2[1]):
            print("%d %.1f"%(1, sale_1))
    elif sale_1 and sale_2 == price:
        print("Nope")
cou(float(input()), input().split(), input().split())
