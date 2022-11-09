"""Impostor"""
import json as j
def get_a_d_im():
    """get alive, get dead, get num impostor"""
    count = 0
    dict_role = {}
    while True:
        role = input()
        if role == "Start":
            break
        res = j.loads(role)
        dict_role.update(res)
    dict_alive = dict_role.copy()
    dict_dead = dict_role.copy()
    while True:
        voteout = input()
        if voteout == "End":
            break
        #เอาคนตายออกก็จะได้คนที่อยู่ต่อ
        for iii in dict_role:
            if voteout == iii:
                dict_alive.pop(iii)
    #เอาตัวซ้ำคนตาย
    for iii in dict_alive:
        for jjj in dict_role:
            if iii == jjj:
                dict_dead.pop(iii)
    #นับimpostor
    for aaa in dict_alive.values():
        if aaa == "Impostor":
            count += 1
    return count, dict_alive, dict_dead
def main():
    """Impostor"""
    count, alive, dead = get_a_d_im()
    print("%d Impostor Remains"%(count))
    print("***Alive***")
    sort_alive = sorted(alive.items(), key=lambda item: item[0])
    for color, imps in sort_alive:
        print("%s : %s"%(color, imps))
    print("***Dead***")
    sort_dead = sorted(dead.items(), key=lambda item: item[0])
    for color, imps in sort_dead:
        print("%s : %s"%(color, imps))
main()
