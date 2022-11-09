"""GCD_v1"""
def gcd(num_x, num_y):
    """GCD_v1"""
    if num_y == 0:
        return num_x
    else:
        return gcd(num_y, num_x%num_y)
print(gcd(int(input()), int(input())))
