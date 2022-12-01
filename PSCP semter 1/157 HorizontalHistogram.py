"""HorizontalHistogram"""
def hor():
    '''Let's see (ไหนดูสิ)'''
    message = input()
    low = {}
    upp = {}
    for i in message:
        if i in low or i in upp:
            continue
        if i.islower():
            low[i] = message.count(i)
        else:
            upp[i] = message.count(i)
    low = (sorted(low.items(), key=lambda x: x[0]))
    upp = (sorted(upp.items(), key=lambda x: x[0]))
    both = dict(low + upp)
    line = ''
    for key, value in both.items():
        for i in range(1, value+1):
            if i%5 == 0 and i != value:
                line += '-|'
            else:
                line += '-'
        print(key, ':', line)
        line = ''
hor()
