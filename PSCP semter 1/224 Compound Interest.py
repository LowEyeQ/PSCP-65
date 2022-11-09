"""Compound Interest"""
def com(baht, interest, years):
    """Compound Interest"""
    for _ in range(years):
        baht *= interest
    print("%.2f"%baht)
com(int(input()), 1+(float(input())/100), int(input()))
