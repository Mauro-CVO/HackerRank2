import collections

def sockMerchant(ar):
    pairs = 0
    pairs_dict = collections.Counter(ar)
    for sock in pairs_dict.values():
        pairs = pairs + sock // 2
    print(pairs)

def run():
    input()
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(ar)

if __name__ == '__main__':
    run()