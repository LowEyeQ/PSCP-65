"""BreachTheDoor"""
def bre(sentence):
    """BreachTheDoor"""
    clean = ["".join(e for e in string if e.isalnum() and not e.isdigit()) for string in sentence]
    ans = [door for door in clean if len(door) > 6]
    print(*ans, end="")
bre(input().split(" "))
