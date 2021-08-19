def solution(a):
    possibles = [0]*len(a)
    
    left_min = a[0]
    right_min = a[-1]
    
    for left_index in range(len(a)):
        right_index = -left_index -1
        
        left_min = min(left_min, a[left_index])
        right_min = min(right_min, a[right_index])
        
        if left_min == a[left_index]:
            possibles[left_index] = 1
        if right_min == a[right_index]:
            possibles[right_index] = 1
            
    answer = possibles.count(1)
    
    
    return answer

    '''
    테스트 1 〉	통과 (0.01ms, 10.2MB)
    테스트 2 〉	통과 (0.01ms, 10.2MB)
    테스트 3 〉	통과 (0.50ms, 10.3MB)
    테스트 4 〉	통과 (49.84ms, 14.4MB)
    테스트 5 〉	통과 (258.43ms, 33.1MB)
    테스트 6 〉	통과 (397.65ms, 44.7MB)
    테스트 7 〉	통과 (497.95ms, 56.3MB)
    테스트 8 〉	통과 (503.28ms, 56.2MB)
    테스트 9 〉	통과 (536.93ms, 56.2MB)
    테스트 10 〉	통과 (517.55ms, 56.2MB)
    테스트 11 〉	통과 (499.14ms, 56.2MB)
    테스트 12 〉	통과 (503.30ms, 56.2MB)
    테스트 13 〉	통과 (516.58ms, 56.2MB)
    테스트 14 〉	통과 (486.63ms, 56.3MB)
    테스트 15 〉	통과 (513.45ms, 56.3MB)
    '''
    
'''
def solution(a):
    for index, num in enumerate(a):
        left_nums = a[:index]
        right_nums = a[index+1:]
        if len(left_nums) != 0 and min(left_nums) < num:
            if  len(right_nums) != 0 and min(right_nums) < num:
                answer -= 1
                
    return answer
'''
