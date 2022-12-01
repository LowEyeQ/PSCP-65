"""Resistor"""
def res(color_1, color_2, color_3, color_4, list_total):
    """Resistor"""
    mean_color = {
        "Black":0,
        "Brown":1,
        "Red":2,
        "Orange":3,
        "Yellow":4,
        "Green":5,
        "Blue":6,
        "Purple":7,
        "Grey":8,
        "White":9,
    }
    multiplier_color = {
        "Black":1,
        "Brown":10,
        "Red":100,
        "Orange":1000,
        "Yellow":10000,
        "Green":100000,
        "Blue":1000000,
        "Purple":10000000,
        "Gold":0.1,
        "Silver":0.01,
    }
    tolerance_color = {
        "Brown":1,
        "Red":2,
        "Green":0.5,
        "Blue":0.25,
        "Purple":0.1,
        "Grey":0.05,
        "Gold":5,
        "Silver":10,
    }
    if (color_2 not in mean_color.keys()) or (color_3 not in multiplier_color.keys()) \
or (color_4 not in tolerance_color.keys()) or (color_1 not in mean_color.keys()):
        print("Error")
    else:
        for iii, aaa in mean_color.items():
            if iii == color_1:
                list_total.insert(0, aaa)
            if iii == color_2:
                list_total.insert(1, aaa)
        for iii, aaa in multiplier_color.items():
            if color_3 == iii:
                list_total.insert(2, aaa)
        for iii, aaa in tolerance_color.items():
            if color_4 == iii:
                list_total.insert(3, aaa)
        ohm = int(str(list_total[0]) + str(list_total[1]))
        # ohm_tolerance = ohm * list_total[3]
        # lower_bound = ohm + ohm_tolerance/100
        # upper_bound = ohm - ohm_tolerance/100
        print("%.4f"%((ohm*list_total[2]) - (ohm*list_total[2]) * (list_total[3]/100)))
        print("%.4f"%((ohm*list_total[2]) + (ohm*list_total[2]) * (list_total[3]/100)))
res(input(), input(), input(), input(), [])
