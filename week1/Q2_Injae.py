def solution(clothes):
    clothes_dict = dict()
    for clt, typ in clothes:
        if typ in clothes_dict.keys():
            clothes_dict[typ] += 1
        else:
            clothes_dict[typ] = 1
    tmp = 1
    for n in clothes_dict.values():
        tmp *= (n+1)
    
    answer =  tmp -1
    return answer

"""
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.2MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
테스트 21 〉	통과 (0.01ms, 10.2MB)
테스트 22 〉	통과 (0.00ms, 10.2MB)
테스트 23 〉	통과 (0.01ms, 10.3MB)
테스트 24 〉	통과 (0.01ms, 10.2MB)
테스트 25 〉	통과 (0.01ms, 10.2MB)
테스트 26 〉	통과 (0.02ms, 10.2MB)
테스트 27 〉	통과 (0.01ms, 10.2MB)
테스트 28 〉	통과 (0.01ms, 10.2MB)
"""
