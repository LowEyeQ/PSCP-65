"""[Recommend] Books"""
from math import ceil
def harry():
    """[Recommend] Books"""
    totalbook = int(input())
    numpage = int(input())
    read_x = int(input())
    read_y = int(input())
    if read_x <= read_y:
        day = 0
        for iii in range(totalbook):
            page = 0
            if ceil(((read_x+day)/(read_y+day))*numpage) >= numpage:
                day += totalbook - iii
                break
            while page < numpage:
                page_1 = ceil(((read_x+day)/(read_y+day))*numpage)
                page += page_1
                day += 1
        print(day)
harry()
