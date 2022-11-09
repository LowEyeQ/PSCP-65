"""RockPaperScissor"""
def rps():
    """RockPaperScissor"""
    yingchub = input()
    team_a = 0
    team_b = 0
    for sums in range(0, len(yingchub), 2):
        if yingchub[sums] == "R" and yingchub[sums+1] == "P":
            team_b += 1
        elif yingchub[sums] == "P" and yingchub[sums+1] == "S":
            team_b += 1
        elif yingchub[sums] == "S" and yingchub[sums+1] == "R":
            team_b += 1
        elif yingchub[sums] == "S" and yingchub[sums+1] == "P":
            team_a += 1
        elif yingchub[sums] == "P" and yingchub[sums+1] == "R":
            team_a += 1
        elif yingchub[sums] == "R" and yingchub[sums+1] == "S":
            team_a += 1
    if team_a > team_b:
        print("A win %d-%d"%(team_a, team_b))
    elif team_a < team_b:
        print("B win %d-%d"%(team_b, team_a))
    else:
        print("DRAW %d"%int(team_a))
rps()
