"""HideAndSeek"""
def hide():
    """HideAndSeek"""
    startma = int(input())
    stopma = int(input())
    stepma = int(input())
    for seek in range(startma, stopma, stepma):
        print(seek)
hide()
