# 8/19
# programmers.co.kr
# 풍선터트리기

def soluiton(a):
    left_min, right_min = float("inf"), float("inf")
    result = [0] * len(a)

    for i in range(len(a)):
        if a[i] < left_min:
            left_min = a[i]
            result[i] = 1
        if a[-1-i] < right_min:
            right_min = a[-1-i]
            result[-1-i] = 1

    return sum(result)

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.22ms, 10.2MB)
# 테스트 4 〉	통과 (13.02ms, 14.4MB)
# 테스트 5 〉	통과 (67.79ms, 32.9MB)
# 테스트 6 〉	통과 (98.10ms, 44.6MB)
# 테스트 7 〉	통과 (130.13ms, 56.3MB)
# 테스트 8 〉	통과 (126.60ms, 56.2MB)
# 테스트 9 〉	통과 (129.94ms, 56.2MB)
# 테스트 10 〉	통과 (132.18ms, 56.1MB)
# 테스트 11 〉	통과 (195.14ms, 56.1MB)
# 테스트 12 〉	통과 (173.44ms, 56.2MB)
# 테스트 13 〉	통과 (168.39ms, 56.1MB)
# 테스트 14 〉	통과 (186.09ms, 56.2MB)
# 테스트 15 〉	통과 (186.35ms, 56.2MB)
