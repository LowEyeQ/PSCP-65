"""Diamond I"""
def dia(row, num):
    """Diamond I"""
    diamond = [0 for _ in range(num)]
    for _ in range(row):
        text = input().split()
        for iii in range(num):
            diamond[iii] += int(text[iii])
    print(max(diamond))
dia(int(input()), int(input()))
