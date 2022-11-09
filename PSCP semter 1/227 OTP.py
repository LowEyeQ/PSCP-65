"""OTP"""
def otp():
    """OTP"""
    while True:
        num = input()
        total = []
        if num == "0":
            break
        for iii in range(len(num)):
            nub = num.count(num[iii][0])
            total.append(nub)
        if max(total) == min(total):
            print("Invalid")
        elif len(num) == 4:
            if total.count(2) == 2:
                print("Valid")
            else:
                print("Invalid")
        elif len(num) == 6:
            if total.count(3) == 3 or total.count(2) == 4:
                print("Valid")
            else:
                print("Invalid")
        else:
            if total.count(2) == 6 or total.count(3) == 6:
                print("Valid")
            else:
                print("Invalid")
otp()
