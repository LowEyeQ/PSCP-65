"""Area"""
def area(row):
    """Area"""
    dict_text = {}
    for _ in range(row):
        text = input()
        for iii in text:
            if iii in dict_text:
                dict_text[iii] += 1
            elif iii == " ":
                pass
            else:
                dict_text[iii] = 1
    print(sum(dict_text.values()))
area(int(input()))
