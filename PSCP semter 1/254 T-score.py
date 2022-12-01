"""T-score"""
from math import sqrt
def tscore(stu_all, _, list_zcore, list_total):
    """T-score"""
    list_score = ([int(input()) for _ in range(stu_all)])
    sum_score = sum(list_score)
    med = (sum_score / stu_all)
    list_sd_1 = sum([list_score[aaa]**2 for aaa in range(stu_all)])
    list_sd = sqrt((stu_all*list_sd_1) - (sum_score**2)) / (stu_all*(stu_all-1))
    if list_sd == 0:
        for iii in range(len(list_score)):
            list_zcore.append(0)
        for iii in range(len(list_score)):
            list_zcore.insert(iii, 50 +(10*list_score[iii]))
        for iii in list_total:
            print("%.2f"%iii)

    else:
        for iii in range(len(list_score)):
            list_zcore.insert(iii, (list_score[iii] - med)/(list_sd))
        for iii in range(len(list_zcore)):
            list_total.insert(iii, 50 + (10*list_zcore[iii]))
        for iii in list_total:
            print("%.2f"%iii)
tscore(int(input()), int(input()), [], [])
