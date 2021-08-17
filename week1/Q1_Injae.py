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

"""
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.66ms, 10.8MB)
테스트 5 〉	통과 (0.72ms, 10.8MB)
테스트 6 〉	통과 (0.62ms, 10.9MB)
테스트 7 〉	통과 (80.75ms, 59.9MB)
테스트 8 〉	통과 (86.44ms, 60MB)
테스트 9 〉	통과 (82.26ms, 60MB)
"""
