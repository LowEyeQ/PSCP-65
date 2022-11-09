""" PhoneNumber """
def phonenumber():
    """ PhoneNumber """
    call = input()
    text = input()
    if text == "Domestic":
        if len(call) == 9:
            print(call[0], call[1:5], call[5:9])
        if len(call) == 10:
            print(call[0:2], call[2:6], call[6:10])
    if text == "International":
        if len(call) == 9:
            print("+66", call[1:5], call[5:9])
        if len(call) == 10:
            print("+66"+call[1], call[2:6], call[6:10])
phonenumber()
