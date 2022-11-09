"""CompositeFunction"""
def fog(value):
    """f(x)"""
    value1 = value*2
    return value1
def guy(value):
    """g(x)"""
    value2 = value/2+1
    return value2
def main():
    """get some input"""
    value = int(input())
    print("%.2f"%fog(guy(value)))
    print("%.2f"%guy(fog(value)))
main()
