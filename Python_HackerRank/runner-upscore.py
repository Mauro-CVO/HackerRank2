
def run(n,arr):
    arr = list(dict.fromkeys(arr))
    arr.pop(arr.index(max(arr)))
    print(max(arr))

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    run(n,arr)