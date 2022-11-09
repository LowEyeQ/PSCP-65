"""Turnstile"""
def stile():
    """Turnstile"""
    total = 0
    unlock = False
    while True:
        var = input()
        if var == "END":
            break
        if var == "C":
            unlock = True
        elif var == "P" and unlock == True:
            total += 1
            unlock = False
    print(total)
stile()



"""Turnstile"""
def main():
    """Turnstile"""
    num = 0
    count = 0
    while True:
        message = input()
        if message == "C":
            num = 1
        if message == "P" and num == 1:
                count += 1
                num = 0
        if message == "END":
            break
    print(count)
main()
