"""LetterFrequency"""
def fre():
    """LetterFrequency"""
    text = input().lower()
    dict_text = {}
    for iii in text:
        if iii in dict_text:
            dict_text[iii] += 1
        elif " " in dict_text:
            dict_text.pop(" ")
        else:
            dict_text[iii] = 1
    ans = max(dict_text.items(), key=lambda k: k[1])
    # ans = max(dict_text, key=dict_text.get)
    print(ans[0])
fre()
