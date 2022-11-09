"""Key"""
def key():
    """check to print Key"""
    idnumber = input()
    totalkeys = idsums(idnumber) + threelast(idnumber)
    count = 0
    for _ in str(totalkeys):#เช็คหลักของkey
        count += 1
    if count > 4:#ค่ามากกว่าสี่หลัก เอาเเค่4หลัก
        print(str(totalkeys)[1:])
    elif count < 4:#น้อยกว่า4หลัก+1000
        print(totalkeys+1000)
    else:
        print(totalkeys)

def idsums(idnumber):
    """sum of idnumber"""
    sums = 0
    for _ in range(len(str(idnumber))):
        digit = int(idnumber) % 10#หารเอาเศษ จะได้ตัวหลังสุดของหลัก
        sums = sums + digit
        idnumber = int(idnumber) // 10#เอาจำนวนเต็ม ตัดตัวที่นำบวกเเล้ว
    return sums

def threelast(idnumber):
    """last three digit*10"""
    return int(idnumber[10:13])*10
key()



# """ Key V2"""
# def main():
#     """ Key """
#     num = input()
#     ans = 0
#     for _ in num:
#         ans += int(_)
#     last = int(num) %1000 * 10
#     mix = ans + last
#     if mix >= 1000:
#         print("%04d" %(mix%10000))
#     else:
#         print("%04d" %(mix + 1000))
# main()
