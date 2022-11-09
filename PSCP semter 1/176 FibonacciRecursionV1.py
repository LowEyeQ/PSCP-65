"""FibonacciRecursionV1"""
def fib(number):
    """FibonacciRecursionV1"""
    if number <= 1:
        return number
    else:
        return fib(number-1) + fib(number-2)
print(fib(int(input())))
