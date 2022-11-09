"""All_Primes"""
def alls(num):
    """All_Primes"""
    counts = 0
    for aaa in range(num+1):
        if aaa > 1:
            for iii in range(2, aaa):
                if aaa%iii == 0:
                    break
            else:
                counts += 1
    print(counts)
alls(int(input()))
