"""Array time"""
def awmannnn():
    """This is so sad can we hit 10k likes?"""
    juan = input().split()
    tuple_all = tuple(juan)
    find = input()
    count = tuple_all.count(find)
    position = tuple_all.index(find)
    for _ in range(0, count):
        print("%d "%(position)* count)
awmannnn()
