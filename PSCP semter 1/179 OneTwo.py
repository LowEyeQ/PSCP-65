"""OneTwo"""
def onetwo(num):
    """OneTwo"""
    list_num = ["1", "2"]
    for _ in range(2, num):
        total = list_num[1] + list_num[0]
        list_num[0] = list_num[1]
        list_num[1] = total
    if num != 1:
        print(list_num[1])
    else:
        print(list_num[0])
onetwo(int(input()))
