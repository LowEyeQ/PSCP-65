"""Mickey"""
def mic(mouse_house):
    """Mickey"""
    pos_mouse = sorted([int(input()) for _ in range(mouse_house)])
    pos_house = sorted([int(input()) for _ in range(mouse_house)])
    print(max([abs(pos_house[iii] - pos_mouse[iii]) for iii in range(len(pos_mouse))]))
mic(int(input()))
