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

def ver(table,queen,obstacles):
    vertical = []
    for o in obstacles:
        for i in range(len(table)):
            for j in range(len(table)):
                if queen[1] == j:
                    coord = [i,j]
                    if coord == o and o[0] < queen[0]  :
                        continue
                    else:
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
'''
def diag2(table,queen,n):
    diag_sup = []
    diag_inf = []
    diag_der = []
    x = 1
    y = 1
    if queen == [0,0] or queen == [n-1,n-1]:
        pass
    else:
        if queen[0] == 0 or queen[1] == 4 or queen[1] == 0 or queen[0] == 4:
            pass
        else :
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
###'''
def diagDer(table,queen,n):
    diag_sup = []
    diag_inf = []
    diag_der = []
    x = 1
    y = 1
    x_max = n - 2
    if queen == [0,n-1]:
        for i in range(n-1):
            coord = [x,x]
            diag_inf.append(coord)
            x +=1
    elif queen == [n-1,0]:
        for i in range(n-1):
            coord = [x_max,x]
            diag_sup.append(coord)
            x += 1
    elif queen == [0,0] or queen == [n-1,n-1]:
        pass
    else:
        for i in range(n-1-queen[1]):
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

    ### '''

def diagIzq(table,queen,n):
    diag_sup = []
    diag_inf = []
    diag_izq = []
    x = 1
    y = 1
    x_max = n - 2
    if queen == [n-1,n-1]:
        for i in range(n-1):
            coord = [x_max,x_max]
            diag_inf.append(coord)
            x -=1
    elif queen == [0,0]:
        for i in range(n-1):
            coord = [x,x]
            diag_sup.append(coord)
            x += 1
    elif queen == [0,n-1] or queen == [n-1,0]:
        pass
    else:
        for i in range(queen[1]):
            coord = [queen[0] - x, queen[1] - x]
            diag_sup.append(coord)
            print('sup:',diag_sup)
            x -= 1
        for j in range( n-1 - queen[0]):
            coord = [queen[0] + y, queen[1] + y]
            diag_inf.append(coord)
            y += 1
            print(diag_inf)
    
    for i in diag_sup:
        diag_izq.append(i)
    diag_izq.append(queen)
    for i in diag_inf:
        diag_izq.append(i)
    return diag_izq


def queens_attack(n,obstacles,queen):
    #create table
    table = table_create(n)
    #obstacles
    obstacles = traductor_lst(obstacles)
    #queen coords
    queen = traductor_coord(queen)
    #coords can attack
    vertical = ver(table,queen,obstacles)
    horizon = hor(table,queen)
    diag_izq = sorted(diagIzq(table,queen,n))
    diag_der = sorted(diagDer(table,queen,n))


    print(diag_der)
    print(diag_izq)
    #print(table)
    #print(horizon)    
    print('ver:',vertical)
    #print(obstacles)
    print(queen)





n = 5
lst = sorted([[5,5],[4,2],[2,3]])
queen=[1,3]
queens_attack(5,lst,queen)

