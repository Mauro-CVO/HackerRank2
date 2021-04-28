def traductor_lst(coords):

    for i in coords:
        i[0] = n - i[0]
        i[1] = i[1] - 1
    return(coords)

def traductor_coord(coords):
    coords[0] = n - coords[0]
    coords[1] = coords[1] - 1
    return(coords)

def table_create(n):
    table = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(j)
        table.append(row)
    return(table)

def ver(table,queen):
    vertical = []
    for i in range(len(table)):
        for j in range(len(table)):
            if queen[1] == j:
                coord = [i,j]
                vertical.append(coord)
    return vertical

def hor(table,queen):
    horizon = []
    for i in range(len(table)):
        for j in range(len(table)):
            if queen[0] == i:
                coord = [i,j]
                horizon.append(coord)
    return horizon

def diag1(table,queen,n):
    diag_sup = []
    diag_inf = []
    diag_izq = []
    x = 1
    y = 1

    for i in range(queen[0]):
        coord = [queen[0] - x, queen[1] - x]
        diag_sup.append(coord)
        x -= 1
    for j in range(queen[1]):
        coord = [queen[0] + y, queen[1] + y]
        diag_inf.append(coord)
        y += 1
                
    
    for i in diag_sup:
        diag_izq.append(i)
    diag_izq.append(queen)
    for i in diag_inf:
        diag_izq.append(i)
    return diag_izq

def diag2(table,queen,n):
    diag_sup = []
    diag_inf = []
    diag_der = []
    x = 1
    y = 1

    for i in range(queen[0]):
        coord = [queen[0] - x, queen[1] + x]
        diag_sup.append(coord)
        x += 1
    for j in range(queen[1]):
        coord = [queen[0] + y, queen[1] - y]
        diag_inf.append(coord)
        y += 1
                
    
    for i in diag_sup:
        diag_der.append(i)
    diag_der.append(queen)
    for i in diag_inf:
        diag_der.append(i)
    return diag_der



def queens_attack(n,k,r_q,c_q,obstacles):
    queen = [r_q,c_q]
    #create table
    table = table_create(n)
    #obstacles
    obstacles = traductor_lst(obstacles)
    #queen coords
    queen = traductor_coord(queen)
    #coords can attack
    vertical = ver(table,queen)
    horizon = hor(table,queen)
    diag_izq = diag1(table,queen,n)
    diag_der = diag2(table,queen,n)







def run():
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0]
    c_q = int(second_multiple_input[1])
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    queens_attack(n, k, r_q, c_q, obstacles)


if __name__ == '__main__':
    run()