"""GCD_v2"""
def gcd2(num_x, num_y):
    """GCD_v2"""
    if num_y == 0:
        return num_x
    else:
        return gcd2(num_y, num_x%num_y)
print(gcd2(int(input()), int(input())))
