"""Run Length Decoding"""
def rld():
    """Run Length Decoding"""
    text = input()
    decode = ''
    count = 0
    while count < len(text):
        first = ""
        while text[count] in "0123456789":
            first += text[count]
            count += 1
        num = int(first)
        character = text[count]
        count += 1
        decode += num*character
    print(decode)
rld()
