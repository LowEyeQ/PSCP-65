"""Donut"""
def donut():
    """Donut"""
    donuta = int(input()) #price
    donutb = int(input()) #amount
    donutc = int(input()) #free
    donutd = int(input()) #want

    promotion = donutb + donutc
    donut_give = (donutd // promotion) * promotion
    donut_pay = (donutd // promotion) * donutb
    if (donutd % promotion) < donutb:
        donut_give += donutd % promotion
        donut_pay += donutd % promotion
    else:
        donut_give += promotion
        donut_pay += donutb
    print(donut_pay * donuta, donut_give)
donut()

"""Donut V2"""
def donut():
    """Donut V2"""
    price = int(input()) #price
    promo = int(input()) #amount
    free = int(input()) #free
    want = int(input())#want
    purchase = want // (promo + free)#ดูว่าได้โปรโมชั่นกี่ครั้ง
    donut = (want // (promo + free) * (promo + free))#ได้โดนัทกี่ชิ้น
    pay = price * promo * purchase#คิดราคาโดนัทที่ซื้อ
    #ดูเงื่อนไขอื่นๆ
    if want % (promo + free) >= promo:
        donut = donut + promo + free
        pay = pay + price * promo
    else:
        buy = want - donut
        donut += buy
        pay = pay + price * buy
    print("%d %d"%(pay, donut))
donut()
