def is_empty(lst):
    if lst:
        return False
    else:
        return True

def getMoneySpent(keyboards, drives, money):
    total = 0
    buy_lst = []
    for i in keyboards:
        for j in drives:
            if money < i + j:
                continue
            else:
                buy_lst.append(i+j)
    if len(buy_lst) == 0:
        total = -1
    else:
        total = max(buy_lst)
        
    print(total)


def run():
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    getMoneySpent(keyboards, drives, b)


if __name__ == '__main__':
    run()