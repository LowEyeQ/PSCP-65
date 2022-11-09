"""PickThemAgain"""
def pic():
    """PickThemAgain"""
    pick = input().split()
    pick.reverse()
    count = 0
    for ooo in pick:
        if float(ooo)%3 == 0 or float(ooo)%5 == 0:
            print(ooo)
        else:
            count += 1
            if len(pick) == count:
                print("Nope")
pic()
