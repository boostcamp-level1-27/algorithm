def solution(n):
    answer = [[0]*i for i in range(1,n+1)]
    x, y = -1, 0
    num = 1
    step = [(0, 1), (-1, -1), (1, 0)]
    dx, dy = step[-1]
    for recur_num in range(n,0,-1):
        for _ in range(recur_num):
            x += dx
            y += dy
            answer[x][y] = num
            num += 1
        dx, dy = step[(n-recur_num)%3]
    
    result = []
    for s in answer:
        result += s
    return result
