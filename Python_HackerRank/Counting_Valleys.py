def counting_valleys(steps, path):
    sea_level = 0
    valleys = 0
    for i in path:
        if i == 'U':
            sea_level += 1
        else:
            sea_level -= 1
        
        if i == 'U' and sea_level == 0:
            valleys += 1
    print(valleys)

def run():
    steps = int(input().strip())

    path = input()

    counting_valleys(steps, path)

if __name__ == '__main__':
    run()
