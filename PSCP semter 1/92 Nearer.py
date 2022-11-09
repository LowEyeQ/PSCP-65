"""Nearer"""
def near():
    """Nearer"""
    alice = int(input())
    bob = int(input())
    icecreamcar = int(input())
    if abs(alice - icecreamcar) < abs(bob - icecreamcar):
        print("%s %d"%("Alice", abs(alice - icecreamcar)))
    elif abs(bob - icecreamcar) < abs(alice - icecreamcar):
        print("%s %d"%("Bob", abs(bob - icecreamcar)))
    elif abs(icecreamcar - bob) == abs(icecreamcar - alice):
        print("%s %d"%("Sundaes", abs(icecreamcar - alice)))
near()
