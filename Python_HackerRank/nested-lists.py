
def run(lst):
    scores = sorted([i[1] for i in lst])
    second_lst = list(dict.fromkeys(scores))
    second = second_lst[1]
    names = sorted([i[0] for i in lst if i[1] == second])
    for name in names: print(name)

if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])
    run(lst)