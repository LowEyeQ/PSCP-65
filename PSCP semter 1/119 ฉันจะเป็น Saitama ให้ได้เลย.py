"""Saitama"""
def sai():
    """Saitama"""
    push_a = int(input())
    sit_b = int(input())
    stand_c = int(input())
    run_d = int(input())
    push_a_day = int(input())
    sit_b_day = int(input())
    stand_c_day = int(input())
    run_d_day = int(input())

    mission_1_days = push_a / push_a_day
    mission_2_days = sit_b / sit_b_day
    mission_3_days = stand_c / run_d_day
    mission_4_days = run_d / stand_c_day

    for _ in range(4):
        if mission_1_days <= mission_2_days:
            mission_1_days, mission_2_days = mission_2_days, mission_1_days
        if mission_2_days <= mission_3_days:
            mission_2_days, mission_3_days = mission_3_days, mission_2_days
        if mission_3_days <= mission_4_days:
            mission_3_days, mission_4_days = mission_4_days, mission_3_days
    print(int(mission_1_days + 0.999999999))
sai()
