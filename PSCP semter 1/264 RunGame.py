""""RunGame"""
def rungame(numrun, dis_total):
    """RunGame"""
    if len(numrun) == 0:
        print(0)
    else:
        dis_total = sum([abs(int(numrun[iii]) - int(numrun[iii+1])) \
    for iii in range(len(numrun)-1)])
        print(dis_total + abs(int(numrun[0])))
rungame(input().split(), [])
