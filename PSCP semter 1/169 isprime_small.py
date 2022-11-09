"""isprime_small"""
def smalls(num):
    """isprime_small"""
    if num > 1:
        for iii in range(2, num):
            if num%iii == 0:
                return "No"
        return "Yes"
    return "No"
print(smalls(int(input())))
