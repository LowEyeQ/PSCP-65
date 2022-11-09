"""Timing"""
def main():
    """Timing"""
    second = int(input())
    minute = second // 60
    second = second % 60
    hour = minute // 60
    minute = minute % 60
    day = hour // 24
    hour = hour % 24
    print(day, hour, minute, second)
main()
