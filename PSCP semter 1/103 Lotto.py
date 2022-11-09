"""Lotto"""
def lot():
    """Lotto"""
    first = input()
    second = input()
    third = input()
    forth = input()
    fifth = input()
    sixth = input()
    mylotto = input()
    result = 0
    if mylotto == first:
        result += 6000000
    if mylotto[-2:] == second:
        result += 2000
    if mylotto[:3] == third and mylotto[:3] == forth:
        result += 8000
    elif mylotto[:3] == third or mylotto[:3] == forth:
        result += 4000
    if mylotto[-3:] == fifth and mylotto[-3:] == sixth:
        result += 8000
    elif mylotto[-3:] == fifth or mylotto[-3:] == sixth:
        result += 4000
    if first == "000000" and (mylotto == "999999" or mylotto == "000001"):
        result += 100000
    elif first == "999999" and mylotto == "000000":
        result += 100000
    elif int(first) - 1 == int(mylotto) or int(first) + 1 == int(mylotto):
        result += 100000
    else:
        result = result
    print(result)
lot()
