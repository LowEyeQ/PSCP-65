"""Filter"""
def clas(tep, data):
    """Filter"""
    while True:
        student_id = input()
        if student_id == "END":
            break
        if student_id[:4] not in data:
            data[student_id[:4]] = 1
        elif student_id[:4] in data:
            data[student_id[:4]] += 1
    sort_data = sorted(data)
    for iii in sort_data:
        if iii[:2] != tep:
            print(iii[:2], int(iii[2:4]), data[iii])
        else:
            print("--", int(iii[2:4]), data[iii])
        tep = iii[:2]
clas("", {})
