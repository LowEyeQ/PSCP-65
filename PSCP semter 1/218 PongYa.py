"""PongYa"""
def pong(nub):
    """PongYa"""
    if nub%3 == 0 or str(nub)[-1] == "3":
        print("PONG")
    else:
        print(nub)
pong(int(input()))
