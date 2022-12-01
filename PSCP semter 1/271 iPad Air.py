""""iPad Air"""
def ipadair(color, capacity, wire):
    """iPad Air"""
    capacity_ipad = [64, 256]
    color_ipad = ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"]
    wire_ipad = ["Wi-Fi + Cellular", "Wi-Fi"]
    if color in color_ipad and capacity in capacity_ipad and wire in wire_ipad:
        ans = check_ipad(capacity, wire)
        print(ans)
    else:
        print("Not Available ")

def check_ipad(capacity, wire):
    """Check ipad"""
    if capacity == 64 and wire == "Wi-Fi":
        return 19900
    elif capacity == 256 and wire == "Wi-Fi":
        return 24900
    elif capacity == 64 and wire == "Wi-Fi + Cellular":
        return 24400
    elif capacity == 256 and wire == "Wi-Fi + Cellular":
        return 29400
    else:
        return "Not Available "

ipadair(input(), int(input()), input())
