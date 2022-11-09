"""ProgressiveTax"""
def pro():
    """ProgressiveTax"""
    total = int(input())
    taxtotal = 0
    if total > 4000000:
        amount = total-4000000
        total -= amount
        taxtotal += amount*0.35
    if total > 2000000:
        amount = total-2000000
        total -= amount
        taxtotal += amount*0.30
    if total > 1000000:
        amount = total-1000000
        total -= amount
        taxtotal += amount*0.25
    if total > 750000:
        amount = total-750000
        total -= amount
        taxtotal += amount*0.20
    if total > 500000:
        amount = total-500000
        total -= amount
        taxtotal += amount*0.15
    if  total > 300000:
        amount = total-300000
        total -= amount
        taxtotal += amount*0.10
    if total > 150000:
        amount = total-150000
        total -= amount
        taxtotal += amount*0.05
    print(int(taxtotal))
pro()
