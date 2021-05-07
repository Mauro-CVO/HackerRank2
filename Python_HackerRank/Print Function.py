if __name__ == '__main__':
    n = int(input())
    lst = list(range(1,n+1))
    print(lst)
    x = 0
    total = 0
    max_n = len(lst)-1
    for i in range(len(lst)):
        if i == 10:
            x = (10**max_n) * 1
        else:
            x = (10**max_n) * lst[i]
        print(x)
        total += x
        print(total)
        max_n -= 1
    
    print(total)
        