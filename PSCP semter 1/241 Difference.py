'''Difference'''
import json as j
def main():
    '''Difference'''
    list_a = j.loads(input().replace("'", '"'))
    list_b = j.loads(input().replace("'", '"'))
    check = True
    result = {}
    for i in set(list_a) - set(list_b):
        result[i] = list_a.count(i)
    for i in set(list_b) - set(list_a):
        result[i] = list_b.count(i)
    for i in list_a:
        if list_a.count(i) != list_b.count(i):
            result[i] = abs(list_a.count(i) - list_b.count(i))
    if result != {}:
        check = False
    result_sorted = sorted(result)
    for i in result_sorted:
        print(i, result[i])
    if check:
        print('ONAJI DAYO!')
main()
