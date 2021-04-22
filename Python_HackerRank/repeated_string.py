import math

def repeated_string(s, n):
    if 'a' not in s:
        print(0)

    elif len(s) == 1:
        print(n)

    else :
    s = s * (n//(len(s)-1))
    s = s[:n]
    for i in s:
        if i == 'a':
            num_a += 1

    print(num_a)
    '''
    c = s.count('a')
    div=n//len(s)
    if n%len(s)==0:
        c= c*div
    else:
        m = n%len(s)
        c= c*div+s[:m].count('a')
    print(c)'''




def run():
    s = input()
    n = int(input())
    repeated_string(s,n)

if __name__ == "__main__":
    run()