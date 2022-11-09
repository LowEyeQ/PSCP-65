"""ISBN"""
def isb(id_isbn):
    """ISBN"""
    if id_isbn[3] == "X":
        id_isbn[3] = 10
        total = -((10*(int(id_isbn[0][0]))) + (9*(int(id_isbn[0][1]))) + (8*(int(id_isbn[0][2]))) \
+(7*(int(id_isbn[1][0])))+(6*(int(id_isbn[1][1])))+(5*(int(id_isbn[1][2]))) \
+(4*(int(id_isbn[2][0]))) + (3*(int(id_isbn[2][1]))) \
+(2*(int(id_isbn[2][2]))))%11
    else:
        total = -((10*(int(id_isbn[0][0]))) + (9*(int(id_isbn[0][1]))) + (8*(int(id_isbn[0][2]))) \
+(7*(int(id_isbn[1][0])))+(6*(int(id_isbn[1][1])))+(5*(int(id_isbn[1][2]))) \
+(4*(int(id_isbn[2][0]))) + (3*(int(id_isbn[2][1]))) \
+(2*(int(id_isbn[2][2]))))%11
    if total == 10:
        if int(id_isbn[3]) == 10:
            print("Yes")
        else:
            print("%s %s"%("No", "X"))
    elif total == int(id_isbn[3]):
        print("Yes")
    else:
        print("%s %d"%("No", total))
isb(input().split("-"))
