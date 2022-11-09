# """Rectangle"""
# def main():
#     """funtion"""
#     high = int(input())
#     wide = int(input())
#     def area():
#         """area Rectangle"""
#         areas = high*wide
#         print(areas)
#     area()
#     def circumferencelength():
#         """circumference length"""
#         circumferencelengths = (2*(high+wide))
#         print(circumferencelengths)
#     circumferencelength()
# main()

""""rectangle V2"""
def test():
    """test"""
    height = int(input())
    weight = int(input())
    print(area(height, weight))
    print(circum(height, weight))
def area(height, weight):
    """area"""
    areas = height * weight
    return areas
def circum(height, weight):
    """circum"""
    lentg = (2*(height+weight))
    return lentg
test()
