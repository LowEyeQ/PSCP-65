"""WeightStation"""
def function():
    """WeightStation"""
    average = float(input())
    wheel2 = float(input())
    wheel3 = float(input())
    wheel4 = float(input())
    wheel1 = (average*4)-wheel2-wheel3-wheel4
    sum1234 = (wheel1+wheel2+wheel3+wheel4)
    if sum1234 <= 15000:
        if(average/2 < wheel1 and wheel1 < average/2+average)and\
(average/2 < wheel2 and wheel2 < average/2+average)and\
(average/2 < wheel3 and wheel3 < average/2+average)and\
(average/2 < wheel4 and wheel4 < average/2+average):
            print("Pass %.2f"%wheel1)
        else:
            print("Unbalance")
    else:
        print("Overweight")
function()
