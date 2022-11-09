"""Seeker"""
import re
def seek():
    """"Seeker"""
    count = 0
    text = input()
    ans = re.findall("[0-9]+", text)
    for iii in ans:
        count += int((iii))
    print(count)
seek()

"""Seeker"""
def main():
    """Seeker"""
    total = ""
    cheat = input()
    for i in cheat:
        if i.isdecimal() == True:
            total += i
        else:
            total += " "
    total = total.split()
    print(sum(list(map(int, total))))
main()
