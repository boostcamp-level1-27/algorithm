def solution(s):
    n = len(s)
    best_minus = 0
    for d in range(1,(n//2)+1):
        current = s[0:d]
        seq = 0
        minus = 0
        for i in range(1,(n//d)+1):
            if current == s[i*d:(i+1)*d]:
                seq += 1
            else:
                current = s[i*d:(i+1)*d]
                if seq > 0:
                    minus += seq*d-1
                    if seq>8:
                        minus -= 1
                    if seq>98:
                        minus -= 1
                    if seq>998:
                        minus -= 1
                    seq = 0
        if seq > 0:
            minus += seq*d-1
            if seq>8:
                minus -= 1
            if seq>98:
                minus -= 1
            if seq>998:
                minus -= 1
        best_minus = minus if best_minus < minus else best_minus
    
    answer = n-best_minus
    return answer
"""
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.50ms, 10.3MB)
테스트 3 〉	통과 (0.23ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.53ms, 10.2MB)
테스트 8 〉	통과 (1.08ms, 10.2MB)
테스트 9 〉	통과 (0.86ms, 10.2MB)
테스트 10 〉	통과 (2.30ms, 10.3MB)
테스트 11 〉	통과 (0.11ms, 10.3MB)
테스트 12 〉	통과 (0.11ms, 10.1MB)
테스트 13 〉	통과 (0.12ms, 10.3MB)
테스트 14 〉	통과 (0.79ms, 10.3MB)
테스트 15 〉	통과 (0.09ms, 10.3MB)
테스트 16 〉	통과 (0.03ms, 10.3MB)
테스트 17 〉	통과 (1.42ms, 10.2MB)
테스트 18 〉	통과 (1.36ms, 10.2MB)
테스트 19 〉	통과 (1.40ms, 10.2MB)
테스트 20 〉	통과 (2.49ms, 10.3MB)
테스트 21 〉	통과 (4.36ms, 10.2MB)
테스트 22 〉	통과 (2.70ms, 10.2MB)
테스트 23 〉	통과 (2.47ms, 10.2MB)
테스트 24 〉	통과 (2.30ms, 10.2MB)
테스트 25 〉	통과 (2.52ms, 10.2MB)
테스트 26 〉	통과 (2.53ms, 10.4MB)
테스트 27 〉	통과 (3.13ms, 10.2MB)
테스트 28 〉	통과 (0.02ms, 10.2MB)
"""
