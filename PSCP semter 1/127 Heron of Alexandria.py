"""Heron of Alexandria"""
from math import sqrt
def her(lenght_1, lenght_2, lenght_3):
    """Heron of Alexandria"""
    text_s = (lenght_1+lenght_2+lenght_3)/2
    print("%.3f"%(sqrt((text_s*(text_s-lenght_1))*(text_s-lenght_2)*(text_s-lenght_3))))
her(float(input()), float(input()), float(input()))
