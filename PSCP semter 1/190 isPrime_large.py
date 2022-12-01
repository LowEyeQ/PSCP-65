"""isprime_large"""
def smalls(num):
    """isprime_small"""
    if num > 1:
        for iii in range(2, int(num**0.5)+1):
            if num%iii == 0:
                return "NO"
        return "YES"
    return "NO"
print(smalls(int(input())))
