"""coinchangerv1"""
def coinchager(coin):
    """coinchangerv1"""
    coin25 = coin//25
    coin10 = (coin%25)//10
    coin5 = ((coin%25)%10)//5
    coin1 = (((coin%25)%10)%5)//1
    print(coin25+coin10+coin5+coin1)
coinchager(int(input()))
