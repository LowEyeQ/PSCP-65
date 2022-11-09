"""CoPrimeV1"""
def coprime(num_x, num_y):
    """CoPrimeV1"""
    if num_y == 0:
        if num_x == 1:
            print("%s\n%d"%("YES", num_x))
        else:
            print("%s\n%d"%("NO", num_x))
    else:
        return coprime(num_y, num_x%num_y)
coprime(int(input()), int(input()))
