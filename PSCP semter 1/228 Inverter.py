"""Inverter"""
def inv(two):
    """inventer"""
    for i in range(len(two)):
        if two[i] == "1":
            two[i] = "0"
        else:
            two[i] = "1"
    if  "1" in two:
        print(int("".join(two)))
inv(list(input()))
