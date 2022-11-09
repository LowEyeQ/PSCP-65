"""Kabata"""
def kab(row):
    """Kabata"""
    list_data = []
    list_tep= []
    for _ in range(row):
        text = input()
        list_data.append(text)
        for i in range(0, len(text), 2):
            if (text[i] == "k" and text[i+1] == "a") or (text[i] == "b" and text[i+1] == "a") or (text[i] == "t" and text[i+1] == "a"):
                print("yes")
                break
            elif (text[i] == "b" and text[i+1] == "a") and (text[i] == "k" and text[i+1] == "a"):
                print("yes")
                break
            else:
                print("no")
                break
kab(int(input()))
