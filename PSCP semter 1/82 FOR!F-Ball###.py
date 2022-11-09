"""FOR!F-Ball"""
def ball():
    """FOR!F-Ball"""
    ballpos = 1
    var = input()
    for balls in var:
        if balls == "A":
            if ballpos == 1:
                ballpos = 2
            elif ballpos == 2:
                ballpos = 1
        elif balls == "B":
            if ballpos == 2:
                ballpos = 3
            elif ballpos == 3:
                ballpos = 2
        elif balls == "C":
            if ballpos == 3:
                ballpos = 1
            elif ballpos == 1:
                ballpos = 3
    print(ballpos)
ball()
        # match var:
        #     case "A":
        #         if var == "A":
        #             ballpos = 2
        #         if var == "B":
        #             ballpos = 1
        #         if var == "C":
        #             ballpos = 3
        #         print(ballpos)
        #         break
        #     case "B":
        #         if var == "A":
        #             ballpos = 1
        #         if var == "B":
        #             ballpos = 3
        #         if var == "C":
        #             ballpos = 2
        #         print(ballpos)
        #         break
        #     case "C":
        #         if var == "A":
        #             ballpos = 3
        #         if var == "B":
        #             ballpos = 2
        #         if var == "C":
        #             ballpos = 1
        #         print(ballpos)
        #         break
