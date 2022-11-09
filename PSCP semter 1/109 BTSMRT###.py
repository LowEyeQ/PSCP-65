# """BTSMRT"""
# def bts():
#     """BTSMRT"""
#     days = input()
#     age = float(input())
#     height = float(input())
#     if days == "Children Day":
#         if age < 14 and height <= 140:
#             print("FREE")
#         else:
#             print("PAY")
#     if days == "Normal Day":
#         if age < 14 and height < 90:
#             print("FREE")
#         else:
#             print("PAY")
#     if days == "Senior Day":
#         if age >= 60:
#             print("FREE")
#         elif age < 14 and height < 90:
#             print("FREE")
#         else:
#             print("PAY")
# bts()

"""BTSMRT"""
def bts():
    """BTSMRT"""
    days = input()
    age = float(input())
    height = float(input())
    one = age < 14 and height <= 140 and days == "Children Day"
    two = age < 14 and height < 90
    three = age >= 60 and days == "Senior Day"
    if one or two or three:
        print("FREE")
    else:
        print("PAY")
bts()
