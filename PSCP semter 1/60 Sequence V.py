# """Sequence V"""
# def seqfive():
#     """Sequence V"""
#     nums = int(input())
#     while True:
#         for _ in range(7):
#             if nums == 0:
#                 break
#             print(nums, end=" ")
#             nums -= 1
#         if nums == 0:
#             break
#         print()
# seqfive()



def main():
    """ Sequence V """
    num = int(input())
    for i in range(0, num):
        if i % 7 == 0 and i != 0:
            print()
        print(num, end=" ")
        num -= 1
main()
