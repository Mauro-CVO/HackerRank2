def password(s):
    lst = []

    for i in s:
        lst.append(str(i)) 
    x= 0
    nums = []
    y=0
    i = 0

    while i < len(s) :
        print('i:',lst[i])
        if i > len(lst):
            break

        elif lst[i].isnumeric():

            if int(lst[i]) != 0:
                ##if i == 0:
                nums.append(lst[i])
                lst.pop(i)
                print(lst)
                print(nums)
                i += 1

            if int(lst[i]) == 0:
                if lst[x+1].isnumeric(): 
                    lst[i] = lst[x+1]
                    nums.pop(y)
                    print(lst)
                    i += 1

        elif lst[i].isupper() and lst[i+1].islower():
            a = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = a
            lst.pop(i+3)
            print(lst)
            i += 1
        
        elif lst[i] == '*':
            lst.pop(i)
            print(lst)
            i += 1
        
        
    
    print(lst)



def run():
    s = input()
    password(s)

if __name__ == '__main__':
    run()