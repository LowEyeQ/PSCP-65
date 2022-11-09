"""Squid Game 3 - Tug-of-War"""
def decide():
    """Squid Game 3 - Tug-of-War"""
    team_a = squida()
    team_b = squidb()
    if team_a > team_b:
        print("B")
    elif team_b > team_a:
        print("A")
    else:
        print("AB")

def squida():
    """Team A"""
    result_a = 0
    for _ in range(1, 11):
        team_a = int(input())
        result_a += int(team_a)
    return result_a

def squidb():
    """Team b"""
    result_b = 0
    for _ in range(1, 11):
        team_b = int(input())
        result_b += int(team_b)
    return result_b
decide()
