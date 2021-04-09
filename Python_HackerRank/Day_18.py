
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

    print(s_ls)


s = input()
palindrome(s)

