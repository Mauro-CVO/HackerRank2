from collections import Counter

def stringAnagram(dictionary, query):
    x= 0

    #for i in dictionary:
    #    for j in query:
    #        if sorted(i) == sorted(j):
    #            x+=1
    #    print(x)

    for i in query:
        x = 0
        for j in dictionary:
            if sorted(i) ==  sorted(j):
                
                x+=1
                #print(x)
        print(x)        

    



if __name__ == '__main__':

    dictionary_count = int(input().strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    stringAnagram(dictionary, query)
