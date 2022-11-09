"""Sequence VII"""
def seqseven():
    """Sequence VII"""
    nums = int(input())
    for iii in range(1, nums+1):
        for jjj in range(1, iii+1):
            print(jjj, end=" ")
        print()
    for iii in range(nums-1, 0, -1):
        for jjj in range(1, iii+1):
            print(jjj, end=" ")
        print()
seqseven()
