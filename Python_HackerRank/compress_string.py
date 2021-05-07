''''
def compress_string(a):
    lst = []
    i = 0
    while True:
        if i == len(a):
            break
        x = 1
        j = i + 1
        while a[i] == a[j]:
            #print(a[i],a[j])
            x += 1
            j += 1
            if j >= len(a):
                break
        lst.append((x,a[i]))
        #print(lst)
        i = j
    result = ''
    for k in lst:
        result += str(k) + ' '
    print(result)

def run():
    n = input()
    lst = [int(i) for i in n]
    #print(lst)
    compress_string(lst)

if __name__ == '__main__':
    run()
###''''

from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])