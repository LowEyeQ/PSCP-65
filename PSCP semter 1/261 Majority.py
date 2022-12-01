"""Majority"""
def maj(_, num_vote, dict_count, check):
    """Majority"""
    list_vote = [int(input()) for _ in range(num_vote)]
    for iii in list_vote:
        if iii in dict_count:
            dict_count[iii] += 1
        else:
            dict_count[iii] = 1

    for iii, aaa in dict_count.items():
        if aaa > num_vote/2:
            print(iii, aaa)
            break
        elif aaa < num_vote/2:
            check += 1
            if check == len(dict_count):
                print(0, max(dict_count.values()))
maj(int(input()), int(input()), {}, 0)
