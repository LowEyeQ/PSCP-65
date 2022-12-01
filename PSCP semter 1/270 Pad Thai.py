"""Pad Thai"""
def padthai(material_list, taste_list, check1, check2):
    """Pad Thai"""
    padthai_aroi = ["Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", "Bean Sprouts", "Noodle", \
    "Chives", "Lime", "Egg", "Oil", "Peanuts"]
    taste_aroi = ["Sweet", "Sour", "Salty"]
    while True:
        material = input()
        if material == "Cook":
            break
        material_list.append(material)

    while True:
        taste = input()
        if taste == "End":
            break
        taste_list.append(taste)

padthai([], [], 0, 0)
