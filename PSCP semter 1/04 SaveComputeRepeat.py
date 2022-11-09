"""SaveComputeRepeat"""
def main():
    """SaveComputeRepeat"""
    start_here = 492137954293754252786
    second = start_here // 1000
    start_here %= 1000
    minute = second // 60
    second %= 60
    hour = minute // 60
    minute %= 60
    day = hour // 24
    hour %= 24
    print(day, hour, minute, second, start_here)
main()
