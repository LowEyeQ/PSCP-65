"""Run Length Encoding"""
def rle():
    """Run Length Encoding"""
    encode = ""
    currentrunchar = ""
    count = 0
    text = input()
    for txt in range(len(text)):
        if txt == 0:
            currentrunchar = text[txt]
            count = 1
        else:
            currentchar = text[txt]
            if currentchar == currentrunchar:
                count += 1
            else:
                encode += str(count) + currentrunchar
                currentrunchar = currentchar
                count = 1
    encode += str(count) + currentrunchar
    print(encode)
rle()
