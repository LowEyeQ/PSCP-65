"""BigFrame"""
def bigfr():
    """BigFrame"""
    text1 = input().rstrip()
    text2 = input().rstrip()
    text3 = input().rstrip()
    text4 = input().rstrip()
    text5 = input().rstrip()
    total = max(len(text1), len(text2),\
len(text3), len(text4), len(text5))
    print("*"*(total + 4))
    print("* %s%s *"%(text1, " "*(total-len(text1))))
    print("* %s%s *"%(text2, " "*(total-len(text2))))
    print("* %s%s *"%(text3, " "*(total-len(text3))))
    print("* %s%s *"%(text4, " "*(total-len(text4))))
    print("* %s%s *"%(text5, " "*(total-len(text5))))
    print("*"*(total + 4))
bigfr()
