"""[Recommend] Milk"""
def milk():
    """[Recommend] Milk"""
    milkperbottle = int(input())
    promotion = int(input())
    exmilk = int(input())
    money = int(input())
    bottles = money//milkperbottle
    covers = bottles
    while covers >= promotion and promotion > 0:
        txt1 = (covers//promotion)*exmilk
        txt2 = covers%promotion
        bottles += txt1
        covers = txt1+txt2
    print(bottles)
milk()
