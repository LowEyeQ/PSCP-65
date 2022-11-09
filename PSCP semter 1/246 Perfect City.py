"""Perfect City"""
from math import sqrt
def per(pickup_x, pickup_y, goal_x, goal_y):
    """Perfect City"""
    total = sqrt((goal_x-pickup_x)**2 + (goal_y-pickup_y)**2)
    print("%.2f"%total)
per(float(input()), float(input()), float(input()), float(input()))
