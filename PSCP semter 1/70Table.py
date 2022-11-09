"""Table l"""
def table():
    """Table l"""
    nums = int(input())
    for row in range(15, 15+1):
        for col in range(1, nums+1):
            print(row, "x", col, "=", row*col)
        print()
table()
