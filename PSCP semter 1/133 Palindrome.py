''' Palindrome '''
def palindrome():
    ''' Palindrome '''
    num = int(input())
    time = input()
    i = 0
    while i != num:
        var = "%02d" % (int(time[-2:]) + 1)
        hours = time[0:2].replace(":", "")
        if int(var) % 60 == 0:
            var = "00"
            var2 = int(hours) + 1
            hours = str(var2)
        if int(hours) % 24 == 0:
            hours = "0"
        time = hours + ":" + var
        if time.replace(":", "") == time.replace(":", "")[::-1]:
            i += 1
            print(time)
palindrome()
