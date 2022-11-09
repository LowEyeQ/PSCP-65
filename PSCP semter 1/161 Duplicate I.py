"""Duplicate I"""
def dup(gr_1, gr_2):
    """Duplicate I"""
    list_gr1 = []
    list_gr2 = []
    #group1
    for _ in range(gr_1):
        student_id1 = input()
        list_gr1.append(student_id1)
    #group2
    for _ in range(gr_2):
        student_id2 = input()
        list_gr2.append(student_id2)
    #Final print
    set_gr1 = set(list_gr1)
    set_gr2 = set(list_gr2)
    ans = sorted(set_gr1.intersection(set_gr2), reverse=True)
    if ans:
        print(*ans, sep="\n")
    else:
        print("Nope")
dup(int(input()), int(input()))
