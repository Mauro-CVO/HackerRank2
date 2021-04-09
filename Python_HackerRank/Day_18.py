
def palindrome(p):
    s_ls = []
    s_ws = s.replace(' ','')
    i = len(s_ws)
    j = 0
    #print(s_ws)

    while i != 0:
        s_ls.append(s_ws[j])
        i = i - 1
        j = j + 1
        print(s_ls)

    
    s_ls1 = []
    s_ls2 = []
    for i in s_ls[:len(s_ls)//2]:
        s_ls1.append(i)
    for i in s_ls[len(s_ls) - len(s_ls)//2:]:
        s_ls2.append(i)
    k = 0
    n = 0
    m = len(s_ls2) - 1
    print(s_ls1[n])
    print(s_ls2[m])
    for i in s_ls1:
        if s_ls1[n] == s_ls2[m]:
            n = n + 1
            m = m - 1
            k = k + 1
        else:
            print ("The word, "+s+", is not a palindrome.")
            break
        if k == len(s_ls1):
            print("The word, "+s+", is a palindrome.")


s = input()
palindrome(s)

