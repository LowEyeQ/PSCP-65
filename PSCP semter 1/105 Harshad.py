'''Harshad'''
def harsh():
    '''Harshad'''
    for _ in range(10):
        num = abs(int(input()))
        total = 0
        for hit in str(num):
            total += int(hit)
        if num == 0:
            print("No")
        elif num % total == 0:
            print("Yes")
        else:
            print("No")
harsh()
