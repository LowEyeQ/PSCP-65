"""ValidVar"""
def valid():
    """ValidVar"""
    punctuations = """!"#$%&'()*+, -./:;<=>?@[\\]^`{|}~"""
    num = '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
    wordbad = 'if', 'else', 'elif', 'while', 'for', 'True', 'False', 'continue', 'break', \
'return', 'is', 'in', 'and', 'or', 'from', 'as', 'pass', 'not', 'def', 'None', 'await', 'import', \
'except', 'raise', 'finally', 'lambda', 'try', 'nonlocal', 'assert', 'del', 'global', \
'with', 'async', 'yeild'
    row = int(input())
    for _ in range(row):
        test = input()
        txt1 = test.startswith(num)
        txt3 = test.startswith(" ") or test.endswith(" ")
        for check in test:
            space = check.isspace()
            if check in punctuations or test in wordbad or test in punctuations or txt1:
                print("Invalid")
                break
            if txt3:
                print("Valid")
                break
            if space:
                print("Invalid")
                break
        else:
            print("Valid")
valid()
