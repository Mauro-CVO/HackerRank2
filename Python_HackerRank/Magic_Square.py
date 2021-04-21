def formingMagicSquare(s):
    m1 = [[8,1,6],[3,5,7],[4,9,2]]
    m2 = [[6,1,8],[7,5,3],[2,9,4]]
    m3 = [[4,9,2],[3,5,7],[8,1,6]]
    m4 = [[2,9,4],[7,5,3],[6,1,8]]
    m5 = [[8,3,4],[1,5,9],[6,7,2]]
    m6 = [[4,3,8],[9,5,1],[2,7,6]]
    m7 = [[6,7,2],[1,5,9],[8,3,4]]
    m8 = [[2,7,6],[9,5,1],[4,3,8]]
    posibilities = [m1,m2,m3,m4,m5,m6,m7,m8]
    
    #equals = []

    '''for matrix in posibilities:
        equal = 0
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i][j] == matrix[i][j]:
                    equal += 1
        equals.append(equal)
    print('equals:',equals)
    index = equals.index(max(equals))
    print(index)
    positions =[]'''
    
    '''for i in range(len(equals)):
        if equals[i] == equals[index]:
            positions.append(i)
    print('positions:',positions)'''
    costs = []

    for matrix in posibilities:
        cost = 0
        for i in range(len(s)):
            for j in range(len(s)):
                cost = cost + abs(s[i][j] - matrix[i][j])
        costs.append(cost)
    
    min_cost = min(costs)
    print(min_cost)


def run():
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    formingMagicSquare(s)

if __name__ == '__main__':
    run()