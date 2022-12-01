import calendar as calen
"""NumDays"""
def numday(day_1, month_1, day_2, month_2):
    """NumDays"""
    obj = calen.Calendar()
    for day in obj.itermonthdays3(2020, month_1):
        print(day)





numday(int(input()), int(input()), int(input()), int(input()))
