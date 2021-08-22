def solution(a):
    left = float("inf")
    right = float("inf")
    answer_list = [0]*len(a)
    for i in range(len(a)):
        if left > a[i]:
            left = a[i]
            answer_list[i] = 1

    for j in range(1,len(a)+1):
        if right > a[-j]:
            right = a[-j]
            answer_list[-j] = 1
    

    return sum(answer_list)
"""
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.20ms, 10.2MB)
테스트 4 〉	통과 (12.91ms, 14.4MB)
테스트 5 〉	통과 (64.03ms, 33MB)
테스트 6 〉	통과 (97.10ms, 44.7MB)
테스트 7 〉	통과 (128.80ms, 56.2MB)
테스트 8 〉	통과 (151.96ms, 56.1MB)
테스트 9 〉	통과 (127.53ms, 56.1MB)
테스트 10 〉	통과 (119.97ms, 56.2MB)
테스트 11 〉	통과 (170.02ms, 56.2MB)
테스트 12 〉	통과 (157.67ms, 56.1MB)
테스트 13 〉	통과 (179.75ms, 56.2MB)
테스트 14 〉	통과 (176.27ms, 56.1MB)
테스트 15 〉	통과 (182.19ms, 56.2MB)
"""
