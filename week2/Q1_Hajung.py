def solution(s):
    min_length = len(s)
    
    for peaceLen in range(1, len(s)//2+1):
        peaces = [s[start:start+peaceLen] for start in range(0, len(s), peaceLen)]
        
        same_peace_count = 1
        composed = []
        for peace_index in range(1, len(peaces)):
            if peaces[peace_index] == peaces[peace_index-1]:
                same_peace_count += 1
            else:
                if same_peace_count == 1:
                    composed.append(peaces[peace_index - 1])
                else:
                    composed.append(str(same_peace_count)+peaces[peace_index - 1])
                    same_peace_count = 1
        if same_peace_count == 1:
            composed.append(peaces[-1])
        else:
            composed.append(str(same_peace_count)+peaces[-1])
        
        composed_str = ''.join(composed)
        min_length = min(min_length, len(composed_str))

    return min_length
'''
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.37ms, 10.1MB)
테스트 3 〉	통과 (0.20ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.2MB)
테스트 7 〉	통과 (0.81ms, 10.3MB)
테스트 8 〉	통과 (0.43ms, 10.3MB)
테스트 9 〉	통과 (0.60ms, 10.1MB)
테스트 10 〉	통과 (2.73ms, 10.4MB)
테스트 11 〉	통과 (0.10ms, 10.1MB)
테스트 12 〉	통과 (0.10ms, 10.2MB)
테스트 13 〉	통과 (0.21ms, 10.1MB)
테스트 14 〉	통과 (0.58ms, 10.4MB)
테스트 15 〉	통과 (0.14ms, 10.1MB)
테스트 16 〉	통과 (0.02ms, 10.1MB)
테스트 17 〉	통과 (1.06ms, 10.2MB)
테스트 18 〉	통과 (2.02ms, 10.2MB)
테스트 19 〉	통과 (1.07ms, 10.2MB)
테스트 20 〉	통과 (2.30ms, 10.2MB)
테스트 21 〉	통과 (2.29ms, 10MB)
테스트 22 〉	통과 (2.30ms, 10.3MB)
테스트 23 〉	통과 (2.36ms, 10.1MB)
테스트 24 〉	통과 (2.08ms, 10.2MB)
테스트 25 〉	통과 (2.27ms, 10.2MB)
테스트 26 〉	통과 (2.26ms, 10.2MB)
테스트 27 〉	통과 (2.70ms, 10.1MB)
테스트 28 〉	통과 (0.02ms, 10.1MB)

'''
