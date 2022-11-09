"""BlackJack"""
def black():
    """Blackjack"""
    num = int(input())
    score = 0
    num1 = 0
    while num > 0:
        text = input()
        if (text == "J") or (text == "Q") or (text == "K"):
            score += 10
        elif text == "A":
            score += 11
            num1 += 1
        else:
            score += int(text)
        if score > 21 and num1 > 0:
            score -= 10
            num1 -= 1
        num -= 1
    print(score)
black()
