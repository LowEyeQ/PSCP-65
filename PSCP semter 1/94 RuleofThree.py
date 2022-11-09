"""RuleofThree"""
def rule():
    """RuleofThree"""
    num = int(input())
    good_price = float(input())
    good_weight = float(input())
    good_p_per_w = good_price/good_weight
    for _ in range(num-1):
        price = float(input())
        weight = float(input())
        p_per_w = price/weight
        if p_per_w < good_p_per_w or (p_per_w == good_p_per_w and price < good_price):
            good_p_per_w = p_per_w
            good_price = price
            good_weight = weight
    print("%.2f %.2f" % (good_price, good_weight))
rule()
