"""MissingCard I"""
def miss():
    """MissingCard I"""
    rank = list("AKQJ23456789") + ["10"]
    suit = ("S", "H", "D", "C")
    deck = []
    for sss in suit:
        for rrr in rank:
            deck.append(rrr+sss)
    deck_left = []
    for _  in range(51):
        card_input = input()
        deck_left.append(card_input)
    print(*set(deck)-set(deck_left))
miss()
