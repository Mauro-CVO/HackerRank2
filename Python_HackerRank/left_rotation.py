def lst2str(arr):
    s = ''
    for i in arr:
        i = str(i)
        s += i
        s += ' '
    print(s)

def left_rotation(arr,d):
    if d ==0:
        lst2str(arr)
    else:
        for _ in range(d):
            popped = arr.pop(0)
            arr.append(popped)
    
    lst2str(arr)

def run():
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    left_rotation(a,d)

if __name__ == '__main__':
    run()