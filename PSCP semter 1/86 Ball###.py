"""ball"""
def ball():
    """ball"""
    balls = float(input())
    time = 0
    while balls >= 0.01:
        if balls >= 0.01:
            balls = 0.6*(balls)
            time += 1
        if balls < 0.01:
            break
    print(time-1)
ball()
