"""Fever"""
def fev(temperature):
    """Fever"""
    if temperature < 36:
        print("hypothermia")
    elif temperature >= 36 and temperature < 38:
        print("No Fever")
    elif temperature >= 38  and temperature < 39:
        print("Mild Fever")
    elif temperature >= 39  and temperature < 40:
        print("High Fever")
    elif temperature >= 40:
        print("Very High Fever")
fev(float(input()))
