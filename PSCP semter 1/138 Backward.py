"""BACKWARD"""
def reverse_time():
    """ARRAY 101"""
    array = []
    while True:
        what = input()
        if what == "NULL":
            break
        array.append(what)
    array.reverse()
    for j in array:
        print(j)
reverse_time()
