"""Guess"""
def gue():
    """Guess"""
    var =  [i for i in range(0, 101)]
    total = []
    mark = "><="
    while True:
        num = input()
        if len(num) == 3:
            break
        else:
            num_list = num.split()
            if num_list[2] == "NO":
                pass
            if num_list[2] == "=":
                total.append()
            elif num_list[0] == ">":
                tep = var.index(int(num_list[1]))
                total.append(var[tep+1:])
            elif num_list[0] == "<":
                tep = var.index(int(num_list[1]))
                total.append(var[tep-1::-1])
    print(total)
gue()

    for yyy, xxx in dict_a.items():
        for zzz, ooo in dict_b.items():
            if xxx == ooo and yyy == zzz:
                dict_total[yyy or zzz] = abs(xxx-ooo)
            elif yyy == zzz:
                dict_total[yyy or zzz] = abs(xxx-ooo)
            else:
                dict_total[yyy or zzz] = xxx
    print(dict_total)
