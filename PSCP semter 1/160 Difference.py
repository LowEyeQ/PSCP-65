"""Difference"""
def diff(num_n, num_m):
    """Difference"""
    set_a, set_b = set(), set()
    #SET A
    for _ in range(num_n):
        a_member = int(input())
        set_a.add(a_member)
    # SET B
    for _ in range(num_m):
        b_member = int(input())
        set_b.add(b_member)
    #final
    total = sorted(set_a - set_b)
    print(*total)
diff(int(input()), int(input()))
