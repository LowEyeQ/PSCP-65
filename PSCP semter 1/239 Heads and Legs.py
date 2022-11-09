"""Heads and Legs"""
def hal(rab_bird, legs):
    """Heads and Legs"""
    if rab_bird == 0 and legs == 0:
        print(0, 0)
    elif legs//4 > rab_bird:
        print("Impossible")




hal(int(input()), int(input()))
