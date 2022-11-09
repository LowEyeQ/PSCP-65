"""Phasmophobia"""
def phas():
    """"Phasmophobia"""
    evidence1 = input()
    evidence2 = input()
    evidence3 = input()
    ghots = [("Banshee","EMF Level 5", "Fingerprints", "Freezing Temperatures"),
("Demon", "Ghost Writing", "Spirit Box", "Freezing Temperatures"),
("Jinn", "EMF Level 5", "Spirit Box", "Ghost Orb"),
("Mare", "Freezing Temperatures", "Spirit Box", "Ghost Orb"),
("Oni", "EMF Level 5", "Spirit Box", "Ghost Writing"),
("Phantom", "EMF Level 5", "Freezing Temperatures", "Ghost Orb"),
("Poltergeist", "Fingerprints", "Spirit Box", "Ghost Orb"),
("Revenant", "EMF Level 5", "Fingerprints", "Ghost Writing"),
("Shade", "EMF Level 5", "Ghost Orb", "Ghost Writing"),
("Spirit", "Fingerprints", "Spirit Box", "Ghost Writing"),
("Wraith", "Fingerprints", "Freezing Temperatures", "Ghost Writing"),
("Yurei", "Ghost Writing", "Freezing Temperatures", "Ghost Orb")]
    dict_ghost = {}
    for iii, evi1, evi2, eve3 in ghots:
        dict_ghost[iii] = evi1, evi2, eve3
    for iii, vvv in dict_ghost.items():
        if evidence1 and evidence2 and evidence3 in vvv:
            print(iii)
        elif evidence1 == "No evidence" or evidence2 == "No evidence" or evidence3 == "No evidence":
            print(iii)
# def checkghost():
#     """CHECK"""
#     evidence1 = input()
#     evidence2 = input()
#     evidence3 = input()
#     if evidence1 and evidence2 and evidence3 in phas():
#         print()
# checkghost()
phas()
