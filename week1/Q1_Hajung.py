def solution(n):
    answer = []
    
    triangle = [[0 for j in range(i)] for i in range(1, n+1)]
    total_len = sum([i for i in range(1, n+1)])
    
    
    #direction = ['down', 'right', 'up']
    direction = 0
    
    i=-1
    j=0
    num = 1
    while num <= total_len:
        if direction == 0:
            i+=1
            while i < n and triangle[i][j] == 0:
                triangle[i][j] = num
                num+=1
                i+=1
            i-=1
            direction = 1
        elif direction == 1:
            j+=1
            while j < n and triangle[i][j] == 0:
                triangle[i][j] = num
                num+=1
                j+=1
            j-=1
            direction = 2
        elif direction == 2:
            i-=1
            j-=1
            while i>=0 and j>=0 and triangle[i][j] == 0:
                triangle[i][j] = num
                num+=1
                j-=1
                i-=1
            i+=1
            j+=1
            direction = 0
    answer = [e for line in triangle for e in line ]
    
    return answer