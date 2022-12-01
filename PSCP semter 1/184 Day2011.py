"""Day 2011"""
def day11(day, month):
    """Day2011"""
    days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    total = days[(day+months[month-1])%7]
    print(total)
day11(int(input()), int(input()))
