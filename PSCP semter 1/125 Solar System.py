"""Solar"""
def solar(text):
    """Solar"""
    where_sun = text.find("Sun")
    if text.find(" Sun ") != -1:
        where_sun = text.find(" Sun ")+1
    elif text.find(" Sun") != -1:
        where_sun = text.find(" Sun")+1
    return where_sun
def main():
    """main"""
    text = input().strip()+" "
    now_planet = ""
    where_sun = solar(text)
    most_hot = ""
    most_cool = ""
    most_hot2 = ""
    most_cool2 = ""
    for numx, i in enumerate(text):
        if i != " ":
            now_planet += i
        if i == " " and numx == text.find(" ") and numx != where_sun+3:
            most_cool = now_planet
        if i == " " and numx == where_sun-1:
            most_hot = now_planet
        if i == " " and numx == text.find(" ", where_sun+4):
            most_hot2 = now_planet
        if i == " " and numx == text.rfind(" ", where_sun+4):
            most_cool2 = now_planet
        if i == " ":
            now_planet = ""
    if text.count(" ", 0, where_sun) == 0:
        print("Hot: %s"%most_hot2)
        print("Cool: %s"%most_cool2)
    elif text.count(" ", where_sun+4) == 0:
        print("Hot: %s"%most_hot)
        print("Cool: %s"%most_cool)
    elif text.count(" ", where_sun+4) > text.count(" ", 0, where_sun):
        print("Hot: %s %s"%(most_hot, most_hot2))
        print("Cool: %s"%(most_cool2))
    elif text.count(" ", where_sun+4) < text.count(" ", 0, where_sun):
        print("Hot: %s %s"%(most_hot, most_hot2))
        print("Cool: %s"%(most_cool))
    else:
        print("Hot: %s %s"%(most_hot, most_hot2))
        print("Cool: %s %s"%(most_cool, most_cool2))
main()
