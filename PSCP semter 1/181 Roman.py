"""Roman"""
def rom(roman):
    """Roman"""
    lookup = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
    }
    count = 0
    last = "I"
    for num in roman[::-1]:
        if lookup[num] < lookup[last]:
            count -= lookup[num]
        else:
            count += lookup[num]
        last = num
    print(count)
rom(input())
