def table_create(n):
    table = []
    for i in range(n):
        row = []
        for j in range(n):
            coord = [i,j]
            row.append(coord)
        table.append(row)
    return(table)

def traductor_lst(coords):

    for i in coords:
        i[0] = n - i[0]
        i[1] = i[1] - 1
    return(coords)

def traductor_coord(coords):
    coords[0] = n - coords[0]
    coords[1] = coords[1] - 1
    return(coords)



def queens_attack(n, obstacles, queen):
    #create table
    table = table_create(n)
    #obstacles
    obstacles = traductor_lst(obstacles)
    #queen coords
    queen = traductor_coord(queen)

    finish = False
    o = 0
    i = 0
    j = 0
    moves = 0
    for o in obstacles:
        print('o:', o)
        for i in table:
            for j in i:
                if queen[1] == j[1] and o[0] > queen[0] and o[0] > j[0]:
                    if queen == j:
                        pass
                    else:
                        moves +=1
                        print('j:',j)
                if queen[1] == j[1] and o[0] < queen[0] and o[0] < j[0]: 
                    if queen == j:
                        pass
                    else:
                        moves +=1
                        print('j:',j)
                if queen[0] == j[0] and o[1] > queen[1] and o[1] > j[1]:
                    if queen == j:
                        pass
                    else:
                        moves +=1
                        print('j:',j)
                if queen[1] == j[1] and o[1] < queen[1] and o[1] < j[1]: 
                    if queen == j:
                        pass
                    else:
                        moves +=1
                        print('j:',j)
        print('-'*20)
    print(moves)

    print(queen)
        

def run():
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])
    queen = [r_q,c_q]
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    queens_attack(n, obstacles, queens)

if __name__ == '__main__':
    
    n = 5
    lst = sorted([[5,5],[4,2],[2,3]])
    queen=[2,3]
    queens_attack(5,lst,queen)