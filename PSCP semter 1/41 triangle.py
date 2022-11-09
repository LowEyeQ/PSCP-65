"""Triangle I"""
def main():
    """Triangle I"""
    wood_a = float(input())
    wood_b = float(input())
    wood_c = float(input())
    if wood_c + 0.01 >= ((wood_a**2 + wood_b**2)**0.5) and \
wood_c - 0.01 <= ((wood_a**2 + wood_b**2)**0.5):
        print("Yes")
    elif wood_b + 0.01 >= ((wood_c**2 + wood_a**2)**0.5) and \
wood_b - 0.01 <= ((wood_c**2 + wood_a**2)**0.5):
        print("Yes")
    elif wood_a + 0.01 >= ((wood_b**2 + wood_c**2)**0.5) and \
wood_a - 0.01 <= ((wood_b**2 + wood_c**2)**0.5):
        print("Yes")
    else:
        print("No")
main()
