"""PRO"""
def pro(come, pay, per_head, pax):
    """PRO"""
    total = (pax//come) * (pay * per_head) + (pax % come * per_head)
    print(int(total))
pro(float(input()), float(input()), int(input()), int(input()))
