# Programmers - 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    answer = 0
    sol = len(s)
    dic = {}

    for i in range(1, len(s) // 2 + 1):
        tempstr = s[0:i]
        tempsol = i + len(s) % i
        tempcnt = 1
        for j in range(i, len(s) + 1 - i, i):
            if tempstr != s[j:j + i]:
                tempstr = s[j:j + i]
                tempsol += i
                if tempcnt > 1:
                    tempsol += len(str(tempcnt))
                tempcnt = 1
            else:
                tempcnt += 1
        if tempcnt > 1:
            tempsol += len(str(tempcnt))
        if tempsol < sol:
            sol = tempsol

    return sol


'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.26ms, 10.3MB)
테스트 3 〉	통과 (0.12ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
테스트 6 〉	통과 (0.03ms, 10.1MB)
테스트 7 〉	통과 (0.33ms, 10.2MB)
테스트 8 〉	통과 (0.28ms, 10.3MB)
테스트 9 〉	통과 (0.46ms, 10.1MB)
테스트 10 〉	통과 (1.64ms, 10.2MB)
테스트 11 〉	통과 (0.06ms, 10.1MB)
테스트 12 〉	통과 (0.06ms, 10.2MB)
테스트 13 〉	통과 (0.08ms, 10.1MB)
테스트 14 〉	통과 (0.42ms, 10.1MB)
테스트 15 〉	통과 (0.07ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.86ms, 10.1MB)
테스트 18 〉	통과 (0.74ms, 10.2MB)
테스트 19 〉	통과 (0.77ms, 10.2MB)
테스트 20 〉	통과 (1.76ms, 10.2MB)
테스트 21 〉	통과 (1.76ms, 10.2MB)
테스트 22 〉	통과 (1.75ms, 10.2MB)
테스트 23 〉	통과 (1.83ms, 10.1MB)
테스트 24 〉	통과 (1.71ms, 10.3MB)
테스트 25 〉	통과 (1.78ms, 10.3MB)
테스트 26 〉	통과 (1.76ms, 10.2MB)
테스트 27 〉	통과 (1.78ms, 10.1MB)
테스트 28 〉	통과 (0.01ms, 10.3MB)
'''