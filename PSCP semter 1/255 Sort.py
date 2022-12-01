"""Sort"""
def sort(list_num):
    """Sort"""
    while True:
        num = input()
        if num == "END":
            break
        else:
            list_num.append(num)
    for iii in range(1, len(list_num)):
        current = list_num[iii]
        while list_num[iii - 1] > current and iii > 0:
            list_num[iii], list_num[iii - 1] = list_num[iii - 1], list_num[iii]
            iii -= 1
    print(list_num)
sort([])
