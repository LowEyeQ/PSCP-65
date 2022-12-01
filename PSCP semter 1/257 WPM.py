"""WPM"""
def wpm(kidsoradults, speed):
    """WPM"""
    if kidsoradults == "Kids":
        for_kids(speed)
    else:
        for_adults(speed)
def for_kids(speed):
    """เด่กน้อยหอยสังข์"""
    if speed < 11:
        print("Very Slow")
    elif 11 <= speed <= 20:
        print("Slow")
    elif 21 <= speed <= 30:
        print("Average")
    elif 31 <= speed <= 40:
        print("Fast")
    else:
        print("Very Fast")
def for_adults(speed):
    """ผู้ ใ ห ญ่"""
    if speed < 26:
        print("Very Slow")
    elif 26 <= speed <= 35:
        print("Slow/Beginner")
    elif 36 <= speed <= 45:
        print("Intermediate/Average")
    elif 46 <= speed <= 65:
        print("Fast/Advanced")
    elif 66 <= speed <= 80:
        print("Very Fast")
    else:
        print("Insane")
wpm(input(), int(input()))
