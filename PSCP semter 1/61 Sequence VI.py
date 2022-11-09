"""Sequence VI"""
def seqsix():
    """Sequence VI"""
    nums = int(input())
    for iii in range(1, nums+1):
        for jjj in range(1, iii+1):
            print(jjj, end=" ")
        print()
seqsix()
