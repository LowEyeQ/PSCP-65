"""RightArrow"""
def right():
    """RightArrow"""
    wide = int(input())
    height = int(input())
    height //= 2
    for row in range(height+1):#Top
        for _ in range(row):#space
            print(" ", end="")
        for _ in range(wide):
            print("*", end="")
        print()
    for row in range(height):#Bottom
        for _ in range(1, height-row):#space
            print(" ", end="")
        for _ in range(wide):
            print("*", end="")
        print()
right()
