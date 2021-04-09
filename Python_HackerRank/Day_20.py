import sys


def bubble_sort(lista):
    n = len(lista)
    Swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                Swaps = Swaps + 1 
    print('Array sorted in',Swaps, 'swaps.')
    print('First Element:', lista[0])
    print('Last Element:', lista[len(lista) - 1])

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

bubble_sort(a)