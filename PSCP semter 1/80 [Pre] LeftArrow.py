"""[Pre] LeftArrow"""
def main():
    """[Pre] LeftArrow"""
    wide = int(input())
    height = int(input())
    space = int((height-1)/2)
    if height%2 == 1:
        for i in range(space, -1, -1):
            print(" "*i, end="")
            print(wide*"*")
        for i in range(1, space+1):
            print(" "*i, end="")
            print(wide*"*")
main()
