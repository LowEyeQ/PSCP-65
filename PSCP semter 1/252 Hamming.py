"""Hamming"""
def ham(txt1, txt2, check):
    """Hamming"""
    for i in range(len(txt1)):
        if txt1[i] != txt2[i]:
            check += 1
    print(check)
ham(input(), input(), 0)
