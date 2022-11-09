"""Median"""
def med():
    """Median"""
    row = int(input())
    data = []
    for _ in range(1, row+1):
        num = float(input())
        data.append(num)
    data.sort()
    numofdata = len(data)
    if numofdata %2 == 0:
        median1 = data[numofdata // 2]
        median2 = data[numofdata // 2 - 1]
        ans = (median1 + median2)/2
    else:
        ans = data[numofdata // 2]
    print(ans)
med()
