"""Runner"""
def main(distance, challgener):
    """runner"""
    timecha = []
    for i in range(challgener):
        numcha = input().split()
        time = (distance - int(numcha[-1])) / int(numcha[0])
        tep = [i+1, int(numcha[0]), time]
        timecha.append(tep)
    timecha.sort(key=lambda items: items[1], reverse=True)
    timecha.sort(key=lambda items: items[2])
    print(timecha)
main(int(input()), int(input()))
