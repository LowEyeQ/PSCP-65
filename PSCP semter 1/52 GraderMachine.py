"""GraderMachine"""
def grades():
    """GraderMachine"""
    weight1 = int(input())
    weight2 = int(input())
    totalodd = 0
    print("pass :", end=" ")
    if weight1 < weight2:
        for grade in range(weight1, weight2+1, +1):
            if grade % 2 == 0:
                totalodd = totalodd + grade
                print("%d" %grade, end=" ")
    else:
        for grade in range(weight1, weight2-1, -1):
            if grade % 2 == 0:
                totalodd = totalodd + grade
                print("%d" %grade, end=" ")
    print()
    print("Sum : %d"%totalodd)
grades()
