"""Point Sorting"""
def poi():
    """Point Sorting"""
    list_1 = []
    testset = int(input())
    for _ in range(testset):
        test1 = int(input())
        list_1 = [input().split()  for _ in range(test1)]
        list_1.sort(key=lambda iii: iii[1], reverse=1)
        list_1.sort(key=sums)
        for jjj in list_1:
            print(*jjj)
def sums(totalsum):
    """SUMs"""
    return int(totalsum[0]) + int(totalsum[1])
poi()
