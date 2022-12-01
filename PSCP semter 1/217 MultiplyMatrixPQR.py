"""IG: few.pz"""
def addlist(num1, num2, de007):
    """fewza007"""
    for _ in range(num1):
        lstf = []
        for _ in range(num2):
            few = int(input())
            lstf.append(few)
        de007.append(lstf)
    return de007

def main():
    """ Main function """
    num1, num2, num3 = int(input()), int(input()), int(input())
    alst = addlist(num1, num2, [])
    blst = addlist(num2, num3, [])
    for i in alst:
        for j in range(len(blst[0])):
            sumbyde, countde = 0, 0;
            for k in i:
                sumbyde += k * int(blst[countde][j])
                countde += 1
            print(sumbyde, end=" ")
        print()
main()
