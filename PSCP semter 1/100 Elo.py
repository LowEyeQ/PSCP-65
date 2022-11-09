"""Elo"""
def elo():
    """Elo"""
    text_ra = int(input())
    text_rb = int(input())
    text_aorb = input()
    eloa = 1/((1+10**((text_rb-text_ra)/400)))
    elob = 1/((1+10**((text_ra-text_rb)/400)))
    if text_aorb == "A":
        print("%.2f"%(eloa))
    else:
        print("%.2f"%(elob))
elo()
