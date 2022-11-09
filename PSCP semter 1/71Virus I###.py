# """Virus I"""
# import re
# def virus():
#     """Virus l"""
#     var = input()
#     print(len(re.findall("o", var)))
# virus()

"""Virus I V2"""
def main():
    """Virus I"""
    virus = input()
    total= 0
    for ooo in virus:
        if ooo == "o":
            total += 1
    print(total)
main()
