"""Remove html tags from a string"""
def remove_html_tags(text):
    """Remove html tags from a string"""
    tmp = ""
    lis = []
    count = True
    if "<" in text:
        for i in text:
            if i == "<":
                count = False
                tmp = tmp.split()
                lis.extend(tmp)
                tmp = ""
            elif i == ">":
                count = True
            elif count:
                tmp += i
        print(lis)
    else:
        lis = text.split()
        print(lis)
remove_html_tags(input())
