"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def swap(valuea, valueb):
    "Swap"
    value = valuea
    valuea = valueb
    valueb = value
    return valuea, valueb

def main():
    """PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
    option = input()
    value1 = float(input())
    value2 = float(input())
    value3 = float(input())

    if value1 > value3:
        value1, value3 = swap(value1, value3)
    if value1 > value2:
        value1, value2 = swap(value1, value2)
    if value2 > value3:
        value2, value3 = swap(value2, value3)

    if option == "Ascend":
        print("%.2f, %.2f, %.2f"%(value1, value2, value3))
    elif option == "Descend":
        print("%.2f, %.2f, %.2f"%(value3, value2, value1))
main()
