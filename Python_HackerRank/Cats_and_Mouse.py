
def catAndMouse(x, y, z):
    cat_a = abs(x - z)
    cat_b = abs(y - z)

    if cat_a == cat_b:
        print('Mouse C')

    elif cat_a < cat_b:
        print('Cat A')
    
    else:
        print('Cat B') 


def  run():
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])

        catAndMouse(x, y, z)

if __name__ == '__main__':
    run()