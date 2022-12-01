"""ATM"""
def atm(list_d_or_w, money_first):
    """ATM"""
    while True:
        depositorwithdraw = input()
        if depositorwithdraw == "END":
            break
        tep = depositorwithdraw.split()
        list_d_or_w.append(tep)
    for i, aaa in list_d_or_w:
        if i == "D":
            money_first += int(aaa)
        elif i == "W":
            if money_first < int(aaa):
                money_first = 0
            else:
                money_first -= int(aaa)
    print(money_first)
atm([], int(input()))
