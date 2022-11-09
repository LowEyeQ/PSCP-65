''' AlmostMean '''
def main():
    ''' AlmostMean '''
    howmuch = int(input())
    idnum = []
    point = []
    for _ in range(howmuch):
        var = input()
        idnum.append(var[0:8])
        var = var[9:].split()
        point.append(''.join(var))
    sumnum = 0
    for _ in range(len(point)):
        num = float(''.join(point[_]))
        sumnum += num
    ave = sumnum/howmuch
    point.append(str(ave))
    point2 = []
    for _ in range(len(point)):
        point2.append(float(point[_]))
    point2 = sorted(point2)
    index2 = int(point2.index(ave))
    ans = point2[index2-1]
    if (str(ans))[-2:] == '.0':
        ans2 = str(ans)[:-2]
    elif (str(ans))[-2:] != '.0':
        ans2 = ans
    indexforid = int(point.index(str(ans)))
    print(idnum[indexforid], ans2, sep="	")
main()
