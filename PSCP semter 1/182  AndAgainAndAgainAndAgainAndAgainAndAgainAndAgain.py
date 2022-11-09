"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def andagain(wordlong, total):
    """"AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
    for iii in range(len(wordlong)):
        count = 0
        for aaa in range(len(wordlong[iii])):
            if wordlong[iii][aaa] in "aeiou":
                count += 1
        if count >= 2:
            total.append(wordlong[iii].strip("."))
    total.sort()
    if len(total) == 0:
        print("Nope")
    else:
        print(*total, sep="\n")
andagain(input().split(), [])
