"""Sequence IV"""
def seqfour():
    """Sequence IV"""
    nums = int(input())
    startna = 1
    for number in range(startna, nums+1):
        for number in range(startna, nums+1):
            print(number, end=" ")
            startna += 1
            nums += 1
        print()
    startna += 1
seqfour()

