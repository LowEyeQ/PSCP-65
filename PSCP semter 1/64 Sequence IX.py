"""Sequence IX"""
def seqnine():
    """Sequence IX"""
    nums = int(input())
    for row in range(nums):
        coun = 1
        for _ in range(nums-row-1):
            print("  ", end=" ")
        for _ in range(1, row+1):
            print("%02d"%coun, end=" ")
            coun += 1
        for _ in range(row+1):
            print("%02d"%coun, end=" ")
            coun -= 1
        print()
seqnine()
