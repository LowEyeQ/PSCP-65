"""Cat Parade"""
def para():
    """Cat Parade"""
    data_list = []
    check = []
    while True:
        species = input()
        if species == "END":
            break
        if "," in species:
            data_list += species.split(", ")
        elif species not in data_list:
            data_list.append(species)
        elif species in data_list:
            data_list.append(species)
        if species == "IT'S A DOG":
            del data_list[-2:]
    for iii in data_list:
        if iii not in check:
            check.append(iii)
    check.sort()
    for aaa in range(0, len(check)):
        print("%s %d %d" %(check[aaa], (data_list.index(check[aaa])+1),\
            data_list.count(check[aaa])))
para()
