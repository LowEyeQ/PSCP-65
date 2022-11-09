"""Ping"""
def ip_address(txt_3):
    """find ip address"""
    counter = txt_3.find(" ")
    sip_address = ""
    while True:
        if txt_3[counter+1] == "[":
            counter = counter + 1
        if txt_3[counter+1:counter+3].isnumeric():
            counter_2 = txt_3[counter+1:].find(" ")+counter
            if txt_3[counter_2] == "]":
                counter_2 = counter_2 - 1
            sip_address += txt_3[counter+1:counter_2+1]
            break
        else:
            counter += txt_3[counter+1:].find(" ") + 1
    return sip_address
def check_lost(txt_4, txt_5, txt_6, txt_7, sip_address):
    """check lost"""
    received = 4
    lost = 0
    if sip_address not in txt_4:
        received -= 1
        lost += 1
    if sip_address not in txt_5:
        received -= 1
        lost += 1
    if sip_address not in txt_6:
        received -= 1
        lost += 1
    if sip_address not in txt_7:
        received -= 1
        lost += 1
    percent_lost = str(int((lost / 4) * 100)) + "%"
    return received, lost, percent_lost
def time_check(con_time):
    """check con time"""
    if con_time[0] == "<":
        return 0
    else:
        return int(con_time[1:])
def check_min_max(min_time, max_time, value):
    """check min max"""
    if min_time > value:
        min_time = value
    if max_time < value:
        max_time = value
    return min_time, max_time
def time(txt_4, txt_5, txt_6, txt_7):
    """find time return it"""
    time_1 = time_2 = time_3 = time_4 = all_time = 0
    min_time = 1000000
    max_time = 0
    if txt_4.find("time") != -1 and txt_4.find("ms") != -1:
        time_1 = time_check(txt_4[txt_4.find("time")+4:txt_4.find("ms")])
        all_time += 1
        min_time, max_time = check_min_max(min_time, max_time, time_1)
    if txt_5.find("time") != -1 and txt_5.find("ms") != -1:
        time_2 = time_check(txt_5[txt_5.find("time")+4:txt_5.find("ms")])
        all_time += 1
        min_time, max_time = check_min_max(min_time, max_time, time_2)
    if txt_6.find("time") != -1 and txt_6.find("ms") != -1:
        time_3 = time_check(txt_6[txt_6.find("time")+4:txt_6.find("ms")])
        all_time += 1
        min_time, max_time = check_min_max(min_time, max_time, time_3)
    if txt_7.find("time") != -1 and txt_7.find("ms") != -1:
        time_4 = time_check(txt_7[txt_7.find("time")+4:txt_7.find("ms")])
        all_time += 1
        min_time, max_time = check_min_max(min_time, max_time, time_4)
    avg_time = int((time_1 + time_2 + time_3 + time_4) / all_time)
    return min_time, max_time, avg_time
def get_value():
    """get value"""
    txt_1 = input()
    txt_2 = input()
    txt_3 = input()
    txt_4 = input()
    txt_5 = input()
    txt_6 = input()
    txt_7 = input()
    return txt_1, txt_2, txt_3, txt_4, txt_5, txt_6, txt_7
def main():
    """print ans"""
    txt_1, txt_2, txt_3, txt_4, txt_5, txt_6, txt_7 = get_value()
    txt_1 = txt_2 = ""
    print(txt_1+txt_2, end="")
    fip_address = ip_address(txt_3)
    received, lost, percent_lost = check_lost(txt_4, txt_5, txt_6, txt_7, fip_address)
    print("Ping statistics for", fip_address + ":")
    print("    Packets: Sent = 4, Received = %d, Lost = %d (%s loss)," \
        %(received, lost, percent_lost))
    if lost != 4:
        print("Approximate round trip times in milli-seconds:")
        print("    Minimum = %dms, Maximum = %dms, Average = %dms" \
            %time(txt_4, txt_5, txt_6, txt_7))
main()
