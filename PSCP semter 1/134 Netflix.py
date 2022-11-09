''' Netflix '''
def netf():
    ''' :_: '''
    mobile, basic, standard, premium, scr, pho = 0, 0, 0, 0, int(input()), int(input())
    _, _ = input(), input()
    on_tv, hd1080, uhd4k = input() == 'Yes', input() == 'Yes', input() == "Yes"
    calct = pho if pho >= scr else scr
    while calct > 0:
        if not (on_tv or hd1080 or uhd4k):
            mobile += calct
            calct -= calct
        elif not (hd1080 or uhd4k):
            if calct >= 4:
                premium += calct // 4
                calct -= (calct // 4) * 4
            elif calct >= 3:
                premium += -(calct // -4)
                calct -= -(calct // -4) * 4
            elif calct >= 2:
                standard += -(calct // -2)
                calct -= -(calct // -2) * 2
            else:
                basic += calct
                calct -= calct
        elif not uhd4k:
            if calct >= 4:
                premium += calct // 4
                calct -= (calct // 4) * 4
            elif calct >= 3:
                premium += -(calct // -4)
                calct -= -(calct // -4) * 4
            else:
                standard += -(calct // -2)
                calct -= -(calct // -2) * 2
        elif uhd4k:
            premium += -(calct // -4)
            calct -= -(calct // -4) * 4
    report(premium, standard, basic, mobile)
def report(premium, standard, basic, mobile):
    ''' :-: '''
    if premium > 0:
        print('Premium x %d' % premium)
    if standard > 0:
        print('Standard x %d' % standard)
    if basic > 0:
        print("Basic x %d" % basic)
    if mobile > 0:
        print("Mobile x %d" % mobile)
    print("Total = %d THB" %((premium*419) + (standard*349) + (basic*279) + (mobile*99)))
netf()
