"""EuclideanDistance"""
def euc(row):
    """EuclideanDistance"""
    dis_list, total = [], []
    for _ in range(row):
        x_and_y = input().split()
        dis_list.append(x_and_y)
    for iii in range(row-1):
        eucdis = (((float(dis_list[iii+1][0]) - float(dis_list[iii][0]))**2) \
+ ((float(dis_list[iii+1][1]) - float(dis_list[iii][1]))**2))**0.5
        total.append(eucdis)
    return "%.2f"%(sum(total))
print(euc(int(input())))
