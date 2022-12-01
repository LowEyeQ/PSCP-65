""""is_prime_LARGER"""
from math import sqrt
def prime(num):
    """"is_prime_LARGER"""
    if num == 2 or num == 3:
        return "True"
    if num % 2 == 0 or num < 2:
        return "False"
    for iii in range(3, int(sqrt(num))+1, 2):
        if num%iii == 0:
            return "False"
    return "True"
print(prime(int(input())))
