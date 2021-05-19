def run(n):
    if n%2 != 0 or (n>5 and n<= 20 and n%2 == 0):
        print('Weird')
    #elif n%2==0 and n<5:
    else:
        print('Not Weird')
        



if __name__ == '__main__':
    n = int(input().strip())
    run(n)