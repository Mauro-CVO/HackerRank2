from collections import Counter

def equalize(a):
    len1 = len(a)
    print(len1)
    a_count = Counter(a)
    most_a = a_count.most_common(1)
    most_a = most_a[0][0]
    print('most_a:', most_a)
    i = 0
    while i < len(a):

        if i > len(a):
            break
        elif a[i] != most_a:
            a.pop(i)
        else:
            i += 1
    #print(a)
    total = len1 - len(a)
    print(total)




def run():
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    equalize(arr)

if __name__ == '__main__':
    run()