"""Olympic"""
def oly(num):
    """Olympic"""
    counts = 1
    olympic_dict = {}
    for _ in range(num):
        country, gold, sliver,bronze  = input().split()
        key = int(gold), int(sliver), int(bronze)
        total = olympic_dict.get(key, [])
        total.append(country)
        olympic_dict[key] = sorted(total)
    print(olympic_dict)
    ans = sorted(olympic_dict, reverse=1)
    for keys in ans:
        for cou in olympic_dict[keys]:
            print(counts, cou, keys[0], keys[1], keys[2], sum(keys))
oly(int(input()))
