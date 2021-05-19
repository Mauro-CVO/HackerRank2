def run(name,marks):
    nums = [i for i in marks.items() if i[0] == name]
    nums = nums[0][1]
    mean = 0
    for i in nums:
        mean += i
    mean = mean/len(nums)
    print("%.2f" % mean)
    
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    run(query_name,student_marks)