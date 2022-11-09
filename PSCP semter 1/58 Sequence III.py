"""Sequence III"""
def seqthree():
    """Sequence III"""
    nums = int(input())
    startna = 1
    for number in range(startna, nums+1):
        for number in range(startna, nums+1):
            print(number+1, end=" ")
        nums += 1
        startna += 1
        number += 1
        print()
seqthree()
 