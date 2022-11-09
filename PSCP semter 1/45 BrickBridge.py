"""BrickBridge"""
def bridge():
    """BrickBridge"""
    brick_s = int(input())
    brick_m = int(input())
    goal = int(input())
    if goal > brick_m*5 + brick_s < goal:
        print("-1")
    elif goal <= brick_m*5 + brick_s:
        if goal == brick_m*5 + brick_s == goal:
            print(brick_s)
        elif goal//5 <= brick_m and brick_s >= (goal-(goal//5)*5):
            print(goal-(goal//5)*5)
        elif goal//5 > brick_m and brick_s >= (goal-(goal//5)*5):
            print(goal-brick_m*5)
        else:
            print("-1")
bridge()

'''BrickBridge V2'''
def main():
    '''input'''
    numa = int(input())
    numb = int(input())
    goal = int(input())
 
    if numb*5 > goal: # ต้องใช้ก้อนใหญ่เท่าไหร่
        how_use = goal //5
    else:
        how_use = numb
    how_use *= 5 # หาว่าใช้ก้อนใหญ่ไปเท่าไหร่
    ans = goal - how_use # หาจำนวนอิฐ
 
    if ans > numa: # ถ้าไม่สามารถสร้างได้
        print(-1)
    else:
        print(ans) # จำนวนอิฐก้อนเล็กที่ต้องใช้
main()
