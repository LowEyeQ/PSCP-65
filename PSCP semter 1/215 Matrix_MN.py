"""Mtrix_MN"""
def martrix(mmm, nnn, result):
    """Mtrix_MN"""
    for _ in range(mmm):
        list_martrix = []
        for _ in range(nnn):
            list_martrix.append(int(input()))
        result.append(list_martrix)
    for iii in range(mmm):
        for jjj in range(nnn):
            print(result[iii][jjj], end=" ")
        print()
martrix(int(input()), int(input()), [])
