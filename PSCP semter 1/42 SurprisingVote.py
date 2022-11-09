"""SurprisingVote"""
def vote():
    """SurprisingVote"""
    total = float(input())
    highest = float(input())
    lowest = total - highest
    if lowest > highest:
        lowest = lowest - highest
        if highest - lowest > 2:
            print("Surprising")
        else:
            print("Not surprising")
    elif highest <= 2:
        print("Not surprising")
    else:
        print("Surprising")
vote()
