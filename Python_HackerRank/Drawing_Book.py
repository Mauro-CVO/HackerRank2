
def page_count(n, p):
    n_new = n //2 + 1
    book = []
    page_izq = 0
    page_der = 1
    der_search = 0
    izq_search = 0
    x = 0
    for i in range(n_new):
        book.append([page_izq, page_der])
        page_izq += 2
        page_der += 2
    book_reverse = book[::-1]
    for i in range(len(book)):
        #print(book[i])
        if p in book[i]:
            der_search = i
            #print(der_search)
    for i in range(len(book_reverse)):
        #print(book_reverse[i])
        if p in book_reverse[i]:
            izq_search = i
    if der_search < izq_search:
        print(der_search)
    else:
        print(izq_search)



if __name__ == '__main__':

    n = int(input())
    p = int(input())
    result = page_count(n, p)