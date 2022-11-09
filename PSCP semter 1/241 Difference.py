"""Difference"""
import json as j
def diffv2(list_a, list_b, dict_a, dict_b, dict_total):
    """["aaa", "aaa", "aaa", "aaa", "ccc","ccc"]"""
    for aaa in list_a:
        dict_a[aaa] = list_a.count(aaa)
    for bbb in list_b:
        dict_b[bbb] = list_b.count(bbb)
    dict_a = sorted(dict_a.items())
    dict_b = sorted(dict_b.items())

diffv2(j.loads(input()), j.loads(input()), {}, {}, {})
