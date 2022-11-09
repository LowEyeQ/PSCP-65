"""HorizontalHistogram"""
def hor(horizon):
    """HorizontalHistogram"""
    dict_horizon = {}
    for iii in horizon:
        dict_horizon[iii] = horizon.count(iii)
    new_dict_horizon = dict(sorted(dict_horizon.items()))
    new_dict_horizon_copy = new_dict_horizon.copy()
    for i, _ in new_dict_horizon.items():
        if i.isupper():
            new_dict_horizon_copy[i] = new_dict_horizon_copy.pop(i)
    for key, value in new_dict_horizon_copy.items():
        if value > 5:
            print("%s : %s"%(key, (value*"-")))
        print("%s : %s"%(key, (value*"-")))
hor(input())
