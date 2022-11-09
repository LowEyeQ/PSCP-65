"""HowLong"""
def coun():
    """HowLong"""
    string = input()
    dcoun = 0
    for total in string:
        if total.isdigit():
            dcoun += 1
    print(dcoun)
coun()
