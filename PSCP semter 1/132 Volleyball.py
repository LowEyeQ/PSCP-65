''' Volleyball '''
def volley():
    ''' Volleyball '''
    var = input()
    apoint = 0
    bpoint = 0
    seta = 0
    setb = 0
    i = 1
    nextset = False
    for _ in var:
        if _ == "A":
            apoint += 1
        elif _ == "B":
            bpoint += 1
        if abs(apoint - bpoint) >= 2:
            if apoint >= (15 if i == 5 else 25) and apoint > bpoint:
                seta += 1
                nextset = True
            if bpoint >= (15 if i == 5 else 25) and apoint < bpoint:
                setb += 1
                nextset = True
        if nextset:
            print("Set %d: A (%d) | B (%d)" %(i, apoint, bpoint))
            i += 1
            apoint = 0
            bpoint = 0
            if seta >= 3 or setb >= 3:
                if seta > setb:
                    print("A won %s:%s set" % (seta, setb))
                else:
                    print("B won %s:%s set" % (setb, seta))
                return
            nextset = False
    print("Set %d: A (%d) | B (%d)\nThe game has not finished yet." % (i, apoint, bpoint))
volley()
