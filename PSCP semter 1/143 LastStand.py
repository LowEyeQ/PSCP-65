"""LastStand"""
def las():
    """"LastStand"""
    stand = input()
    data = stand.strip("][").split(",")
    for last in data:
        print(last[-1])
las()
