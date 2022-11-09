"""LargestNumber"""
def large():
    """LargestNumber"""
    num = int(input())
    num1 = int(input())
    num2 = int(input())
    sums = int(str(num) + str(num1) + str(num2))
    sum1 = int(str(num) + str(num2) + str(num1))
    sum2 = int(str(num1) + str(num) + str(num2))
    sum3 = int(str(num1) + str(num2) + str(num))
    sum4 = int(str(num2) + str(num1) + str(num))
    sum5 = int(str(num2) + str(num) + str(num1))
    largest = 0
    if int(sums) > largest:
        largest = sums
    if int(sum1) > largest:
        largest = sum1
    if int(sum2) > largest:
        largest = sum2
    if int(sum3) > largest:
        largest = sum3
    if int(sum4) > largest:
        largest = sum4
    if int(sum5) > largest:
        largest = sum5
    print(largest)
large()
