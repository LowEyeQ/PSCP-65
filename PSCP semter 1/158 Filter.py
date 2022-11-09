"""Filter"""
import json
def fil(big, score):
    """Filter"""
    dict_big = json.loads(big)
    new_big_dict = dict(sorted(dict_big.items(), key=lambda item: item[0]))
    count = 0
    for key, value in new_big_dict.items():
        if value >= score:
            print("%s	%.2f"%(key, value))
        else:
            count += 1
            if count == len(new_big_dict):
                print("Nope")
fil(input(), float(input()))
