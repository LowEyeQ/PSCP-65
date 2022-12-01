"""Dart"""
def dar(darts, counts):
    """Dart"""
    for _ in range(darts):
        num_darts = input().split()
        pos_x = int(num_darts[0])
        pos_y = int(num_darts[1])
        rasdius = ((pos_x ** 2) + (pos_y ** 2)) ** 0.5
        if rasdius <= 2:
            counts += 5
        elif rasdius <= 4:
            counts += 4
        elif rasdius <= 6:
            counts += 3
        elif rasdius <= 8:
            counts += 2
        elif rasdius <= 10:
            counts += 1
    print(counts)
dar(int(input()), 0)
