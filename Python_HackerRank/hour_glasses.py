

def hour_glass(arr):
    sums = []
    for i in range(len(arr)):
        if i == 0 or i == len(arr)-1:
            pass
        else:
            for j in range(len(arr)):
                if j ==0 or j == len(arr)-1:
                    pass
                else:
                    diag = arr[i+1][j+1] + arr[i-1][j-1] + arr[i+1][j-1] +arr[i-1][j+1] 
                    ver = arr[i+1][j] + arr[i-1][j]
                    sums.append(diag + ver + arr[i][j])
    max_sum = max(sums)
    print(max_sum)

def run():
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    hour_glass(arr)

if __name__ == '__main__':
    run()