"""Sequence N"""
def seqn():
    """Sequence N"""
    nums = int(input())
    for row in range(nums):
        for col in range(nums):
            if col == 0 or col == nums - 1 or (row == col):
                print("*", end="")
            else:
                print(end=" ")
        print()
seqn()
