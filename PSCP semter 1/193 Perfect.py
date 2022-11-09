"""Perfect"""
def per(num, ans):
    """proper divisors """
    for iii in range(1, num//2+1):
        if num%iii == 0:
            ans.append(iii)
    print(sum(ans))
per(int(input()), [])
