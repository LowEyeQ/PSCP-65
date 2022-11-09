"""MyMath"""
import math
def main():
    """MyMath"""
    cos_s = math.cos(math.radians(245**2))+math.cos(math.radians(45+135))
    sin_s = math.sin(math.radians(90))+math.sin(math.radians(60))**2
    log_s = ((math.log(777, 7))-(math.log(888, 8))-(math.log(999, 9)))
    log1 = (math.log(4234, 5))+(math.log(8191, 2))+(71*math.log(156154, 10))
    num = math.sqrt((25-12)**2+(12-15)**2)
    num1 = 15+25
    print(sin_s/cos_s)
    print(math.factorial(16)*math.factorial(4)/(math.factorial(8)))
    print(num1 / num)
    print(math.log(1234**4, 10))
    print(log1/log_s)
main()
