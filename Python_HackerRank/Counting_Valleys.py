def counting_valleys(steps, path):
    sea_level = 1
    y_plus = 0
    y _minus= 0
    way = 1
    for i in range(len(path)):
        if path[i] == 'U':
            y_plus += 1
            way = y_plus + way
        elif path[i] == 'D':
            y_minus -= 1
            way = y_minus + way
        
        
    print('x: ',x, 'y: ',y)
    print(final)


def run():
    steps = int(input().strip())
    path = input().strip()
    
    counting_valleys(steps, path)

if __name__ == '__main__':
    run()