"""WHERE' S THE NUMBER"""
def gone():
    """missing poster here"""
    all_number = []
    nnnn = int(input())
    while True:
        number = int(input())
        if number == 0:
            break
        all_number.append(number)
    all_number.sort()
    for i in range(1, nnnn+1):
        if not i in all_number:
            print(i)
gone()
