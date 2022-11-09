"""WordSequence I"""
def seqword():
    """WordSequence I"""
    text = input()
    len_text = len(text)
    for iii in range(len_text):
        count = 0
        for _ in range(iii+1):
            print(text[count], end="")
            count += 1
        print()
seqword()
