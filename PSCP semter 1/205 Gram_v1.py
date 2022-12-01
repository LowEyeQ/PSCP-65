"""Gram_v1"""
def gramv1(text, count, list_text):
    """Gram_v1"""
    for iii in range(len(text)-1):
        list_text.append(text[iii:iii+2])
    for jjj in range(len(list_text)):
        if list_text.count(list_text[jjj]) > count:
            count = list_text.count(list_text[jjj])
            ans = [list_text[jjj], list_text.count(list_text[jjj])]
    print(*ans, sep="\n")
gramv1(input(), 0, [])
