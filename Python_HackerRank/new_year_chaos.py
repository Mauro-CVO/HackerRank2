
def min_bribes(q):
    pass



def run():
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)


if __name__ == "__main__":
    run()