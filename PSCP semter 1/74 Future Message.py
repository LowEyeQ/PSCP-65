"""Future Message"""
def future():
    """Future Message"""
    var = input()
    if var.isdigit():
        print("Number")
    elif var.isupper():
        print("Uppercase")
    elif var.islower():
        print("Lowercase")
    elif var.istitle():
        print("Title")
    elif var.isspace():
        print("Space")
    else:
        print("Other")
future()
