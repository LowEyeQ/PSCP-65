''' Meteorite '''
def meteorite():
    ''' Meteorite '''
    aaa = float(input())
    bbb = int(input())
    ccc = float(input())
    i = 0
    result = 0
    while ccc <= aaa:
        aaa /= bbb
        result += bbb**i
        i += 1
    print(result)
meteorite()
