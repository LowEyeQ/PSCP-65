"""Diginity"""
def dig():
    """Diginity"""
    while True:
        var = input()
        if var == "0":
            break
        total = 0
        while True:
            for check in str(var):
                total += int(check)
            var = total
            if len(str(var)) == 1:
                print(var)
                break
            total = 0
dig()
