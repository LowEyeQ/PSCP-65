"""Colors"""
def colors(color_1, color_2):
    """Color"""
    primary = "Red", "Yellow", "Blue"
    if color_1 and color_2 in primary:
        if color_1 == color_2:
            print(color_1 or color_2)
        elif color_1 == "Red" and color_2 == "Yellow" or color_1 == "Yellow" and color_2 == "Red":
            print("Orange")
        elif color_1 == "Red" and color_2 == "Blue" or color_1 == "Blue" and color_2 == "Red":
            print("Violet")
        elif color_1 == "Yellow" and color_2 == "Blue" or color_1 == "Blue" and color_2 == "Yellow":
            print("Green")
        else:
            print("Error")
    else:
        print("Error")
colors(input(), input())
