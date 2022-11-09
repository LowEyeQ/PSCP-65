"""FibonacciRecursionV2"""
def fib(number):
    """FibonacciRecursionV2"""
    if number < 2:
        return number
    else:
        return fib(number-1) + fib(number-2)
print(fib(int(input())))
