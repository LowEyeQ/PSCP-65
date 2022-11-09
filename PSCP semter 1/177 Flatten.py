"""Flatten"""
import json as j
def fla():
    """Flatten"""
    list_big = input()
    my_list = j.loads(list_big)
    flat_list = []
    while my_list:
        eee = my_list.pop()
        if isinstance(eee, list):
            my_list.extend(eee)
        else:
            flat_list.append(eee)
    flat_list.sort(reverse=1)
    print(flat_list)
fla()
