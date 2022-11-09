"""BookWorm"""
def main():
    """BookWarm"""
    for _ in range(int(input())):
        time_have, all_book = int(input()), int(input())
        books = sorted([int(input()) for i in range(all_book)])
        temp = []
        for i in books:
            if sum(temp) + i > time_have:
                break
            else:
                temp.append(i)
        print(len(temp))
main()
