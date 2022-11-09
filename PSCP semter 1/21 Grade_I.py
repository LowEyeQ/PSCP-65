"""Grade I"""
def main():
    """print Grade"""
    grade = float(input())
    if 0 <= grade <= 100:
        if grade >= 60:
            print("Pass")
        else:
            print("Fail")
    else:
        pass
main()
