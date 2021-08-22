def solution(n):
    # if n == 4 --> list_n = [[0],[0,0],[0,0,0],[0,0,0,0]]
    list_n = []
    for i in range(1,n+1):
        list_n.append([0 for x in range(i)])
        
    # "fill triangle" function
    def fill_tri(start, num):
        head = start
        list_n[head[0]][head[1]] = num
        num +=1
        #shift left down
        while head[0]+1 < n :
            if list_n[head[0]+1][head[1]] == 0:
                head = [head[0]+1, head[1]]
                list_n[head[0]][head[1]] = num
                num += 1
            else:
                break
        #shift right
        while head[1]+1 < n :
            if list_n[head[0]][head[1]+1] == 0:
                head = [head[0], head[1]+1]
                list_n[head[0]][head[1]] = num
                num += 1
            else:
                break
        #shift up
        while head != start :
            if list_n[head[0]-1][head[1]-1] == 0:
                head = [head[0]-1, head[1]-1]
                list_n[head[0]][head[1]] = num
                num+=1
            else :
                break
        return num
    
    num = 1
    
    # list_n을 순회하면서 0,0이면 fill_tri 함수 실행
    for i in range(n):
        for j in range(i+1):
            if list_n[i][j] == 0:
                num = fill_tri([i,j], num)
                
    answer = []
    for lst in list_n:
        answer += lst
        
    return answer
 

"""
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (3.50ms, 10.9MB)
테스트 5 〉	통과 (3.98ms, 10.9MB)
테스트 6 〉	통과 (2.05ms, 10.8MB)
테스트 7 〉	통과 (296.52ms, 58.6MB)
테스트 8 〉	통과 (314.88ms, 60.3MB)
테스트 9 〉	통과 (233.89ms, 60.3MB)
"""
