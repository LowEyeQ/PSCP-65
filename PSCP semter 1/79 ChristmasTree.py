"""ChristmasTree"""
def tree():
    """ChristmasTree"""
    even = int(input())
    trunk = int(input())
    for christmastree in range(even):
        print(" "*(even-1-christmastree)+"*"*christmastree+"*"*christmastree+"*")#ดาว
    for _ in range(1, trunk+1):
        print("---".center(even*2-1//2))#ลำต้นลำใจ
tree()

