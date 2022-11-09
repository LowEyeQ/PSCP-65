"""Calaculator"""
def cala(total):
    """Calaculator"""
    number = 0
    if total == 1:
        print(1)
    else:
        for iii in range(1, total+1):
            number += len(str(iii))+1
        print(number)
cala(int(input()))
