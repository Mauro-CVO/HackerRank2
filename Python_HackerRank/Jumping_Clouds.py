def jumping_clouds(clouds):
    position = 0
    i = 0
    jump = 0
    x = len(clouds)-1
    #print('x:', x)
    #print('len:',len(clouds))
    while i < x:

        if i == x-1:
            jump += 1
            i += 2
            #print('i: ', i)

        elif clouds[i+2] == 0:
            position = position + 2
            jump += 1
            i = i + 2
            #print('i: ', i)
        
        elif clouds[i+2] == 1:
            position = position + 1
            jump += 1
            i = i + 1

            #print('i: ', i)

    print(jump)

def run():
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    jumping_clouds(c)




if __name__ == '__main__':
    run()
