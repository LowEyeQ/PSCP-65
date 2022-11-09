"""Stepper II"""
def stepperll():
    """Stepper II"""
    startma = int(input())
    stopma = int(input())
    if startma < stopma:
        for desend in range(startma, stopma+1, +1):
            print(desend)
    else:
        for ascend in range(startma, stopma-1, -1):
            print(ascend)
stepperll()
