"""TheFunctionWithin"""
def fog(value):
    """f(x)"""
    value1 = value*2
    return value1
def guy(value):
    """g(x)"""
    value2 = (3*value**4)-(value**3)+(2*value**2)+10
    return value2
def home(valuex, valuey, valuez):
    """h(x,y,z)"""
    value3 = ((valuez+valuex)**2)-(valuex*valuey)+(valuey**2)
    return value3
def ice(valuea, valueb, valuec, valued):
    """i(a,b,c,d)"""
    value4 = ((valuea**2)+(valueb**2)-(valuec**2))\
        /((valued**2)-(2*(valuea*valued))+(2*(valuea)))
    return value4
def main():
    """get some input"""
    valuea = float(input())
    valueb = float(input())
    valuec = float(input())
    valued = float(input())
    print(fog(fog(valuea)))
    print(guy(fog(valuea-valueb)))
    print(home(fog(valuea+valueb), fog(valuea+valuec), guy(fog(valued**2))))
    fun1 = home(fog(valuea+valueb), fog(valuea-valuec), guy(fog(valued**2)))
    fun2 = guy(fog(valuea-valueb))
    fun3 = fog(fog(fog(fog(fog(valuec)))))
    fun4 = valued**8
    print(ice(fun1, fun2, fun3, fun4))
main()
