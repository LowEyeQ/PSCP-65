"""SAFE"""
def saf(openchest, lockchest, counts):
    """SAFE"""
    for iii in range(len(openchest)):
        diff = abs(ord(openchest[iii]) - ord(lockchest[iii]))
        if diff > 13:
            counts += 26 - diff
        else:
            counts += diff
    print(counts)
saf(input(), input(), 0)
