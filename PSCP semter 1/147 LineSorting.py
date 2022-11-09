"""LineSorting"""
def line():
    """LineSorting"""
    row = int(input())
    ans = []
    list_1 = list()
    for _ in range(row):
        text = input()
        ans.append(text)
    for aaa in ans:
        list_1.append((len(aaa), aaa))
    list_1.sort()
    res = list()
    for _, aaa in list_1:
        res.append(aaa)
    for total in res:
        print(total)
line()
