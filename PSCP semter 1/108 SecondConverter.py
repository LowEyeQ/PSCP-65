"""SecondConverter"""
def secconver():
    """SecondConverter"""
    timetest = int(input())#Unit second
    secondparallel = int(input())#1นาทีของโลกคู่ขนานจะมีระยะเวลา s วินาที
    minuteparallel = int(input())#1ชม.ของโลกคู่ขนานจะมีเวลา m นาที
    hourparallel = int(input())#1วันมี h ชั่วโมง
    total_hr = (timetest // (secondparallel * minuteparallel)) % hourparallel
    total_minute = (timetest // secondparallel) % minuteparallel
    total_second = timetest % secondparallel
    print("%d:%d:%d"%(total_hr, total_minute, total_second))
secconver()
