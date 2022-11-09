"""Inflation"""
def inf():
    """Inflation"""
    money = float(input())
    year = int(input())
    money = int(money*100)
    for _ in range(year):
        digit = money*381
        money = money+digit//10000
    digit = str(money)[-2:]
    money = str(money)[:-2]
    if money == "":
        money = "0"
    print("%d.%02d"%(int(money), int(digit)))
inf()

