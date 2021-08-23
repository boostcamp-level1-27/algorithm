# Programmers - 풍선 터트리기
# https://programmers.co.kr/learn/courses/30/lessons/68646#

def solution(a):
    answer = 0
    la = len(a)

    if la == 1:
        return 1
    elif la == 2:
        return 2

    min_lefts = [0]*la
    min_rights = [0]*la

    min_left = a[0]
    min_lefts[0] = a[0]
    min_right = a[-1]
    min_rights[-1] = a[-1]

    for i in range(la-1, -1, -1):
        if min_right > a[i]:
            min_right = a[i]
        min_rights[i] = min_right

    for pi in range(1, len(a) - 1):
        pivot = a[pi]

        if min_left > pivot:
            min_left = a[pi]
        min_lefts[pi] = min_left

        if not (pivot > min_lefts[pi-1] and pivot > min_rights[pi+1]):
            answer += 1

    answer += 2
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.25ms, 10.1MB)
테스트 4 〉	통과 (33.99ms, 15.2MB)
테스트 5 〉	통과 (122.66ms, 36.7MB)
테스트 6 〉	통과 (181.50ms, 50.3MB)
테스트 7 〉	통과 (244.02ms, 63.9MB)
테스트 8 〉	통과 (251.64ms, 63.9MB)
테스트 9 〉	통과 (243.85ms, 63.9MB)
테스트 10 〉	통과 (272.31ms, 63.8MB)
테스트 11 〉	통과 (253.88ms, 63.7MB)
테스트 12 〉	통과 (259.10ms, 63.7MB)
테스트 13 〉	통과 (253.94ms, 63.9MB)
테스트 14 〉	통과 (271.64ms, 63.8MB)
테스트 15 〉	통과 (279.18ms, 64MB)
'''