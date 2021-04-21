def bonAppetit(bill, i, pay):
    bill[i] = 0
    total = 0
    for i in bill:
        total = total + i
    total = total/2
    if total == pay:
        print("Bon Appetit")
    else:
        overcharged =int(pay - total)
        print(overcharged)


def run():
    nk = input().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)





if  __name__ == '__main__':
    run()