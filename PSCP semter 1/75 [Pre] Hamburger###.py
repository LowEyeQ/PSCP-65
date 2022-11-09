"""[Pre] Hamburger"""
def main():
    """[Pre] Hamburger"""
    bread1 = int(input())
    bread2 = int(input())
    totalbread1 = bread1*"|"
    totalbread2 = bread2*"|"
    totalpork = (bread1 + bread2)*2
    pork = "*"*totalpork
    print("%s%s%s"%(totalbread1, pork, totalbread2))
main()
