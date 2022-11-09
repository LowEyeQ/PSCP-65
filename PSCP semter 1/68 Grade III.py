"""Grade III"""
def grade3():
    """Grade III"""
    rows = int(input())
    total = 0
    for _ in range(rows):
        score = float(input())
        if 95 <= score <= 100:
            total += 4
        elif 90 <= score < 95:
            total += 3.5
        elif 85 <= score < 90:
            total += 3
        elif 80 <= score < 85:
            total += 2.5
        elif 75 <= score < 80:
            total += 2
        elif 70 <= score < 75:
            total += 1.5
        elif 65 <= score < 70:
            total += 1
        elif 60 <= score < 65:
            total += 0.5
        elif 0 <= score < 60:
            total += 0
    result = ((total/rows)*100)/100
    print("%0.2f"%result)
grade3()

