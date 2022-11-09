"""B - Fully pair?"""
def fully(text):
    """B - Fully pair?"""
    check = ""
    result = ""
    for char in text:
        if char in check:
            continue
        if text.count(char)%2 != 0:
            result += char
        check += char
    print("fully paired" if len(result) == 0 else result)
fully(input().lower())
