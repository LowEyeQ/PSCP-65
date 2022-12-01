"""SAFE"""
def saf(ope_chest, lockchest, counts):
    """SAFE"""
    for iii in range(len(ope_chest)):
        diff = abs(ord(ope_chest[iii]) - ord(lockchest[iii]))
        if diff > 13:
            counts += 26 - diff
        else:
            counts += diff
    print(counts)
saf(input(), input(), 0)
