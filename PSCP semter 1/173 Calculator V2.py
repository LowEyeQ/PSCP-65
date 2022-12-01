"""Calaculator"""
def cala(total):
    """Calaculator"""
    ans = 0
    lenght = len(str(total))
    if total == 1:
        print(1)
    elif len(str(total)) == 1:
        print(total*2)
    else:
        for i in range(lenght, 0, -1):
            if i == lenght:
                ans += (total - int('9'*(lenght-1)))*lenght
            else:
                ans += 9*(10**(i-1))*i
        print(ans + total)
cala(int(input()))
