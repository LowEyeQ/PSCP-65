"""PickThem"""
import json as j
def them():
    """PickThem"""
    total = 0
    pick = input()
    data = j.loads(pick)
    for ooo in data:
        if ooo%2 == 0:
            print(ooo)
        elif ooo%2 != 0:
            total += 1
            if total == len(data):
                print("Nope")
them()
