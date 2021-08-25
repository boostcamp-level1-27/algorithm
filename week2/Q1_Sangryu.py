# 8/23
# programmers.co.kr
# 문자열압축

def solution(s):
    concat_list = []
    if len(s) == 1:
        return 1

    for length in range(1, (len(s) // 2) + 1):
        concat = ''
        count = 1
        compare_s = s[:length]

        for j in range(length, len(s), length):

            if compare_s  == s[j : length+j]:
                count += 1
            else:
                if count != 1:
                    concat += str(count) + compare_s
                else:
                    concat += compare_s

                compare_s = s[j : j + length]
                count = 1

        if count != 1:
            concat += str(count) + compare_s
        else:
            concat += compare_s

        concat_list.append(len(concat))

    return min(concat_list)

# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.30ms, 10.2MB)
# 테스트 3 〉	통과 (0.16ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.00ms, 10.2MB)
# 테스트 6 〉	통과 (0.03ms, 10.2MB)
# 테스트 7 〉	통과 (0.35ms, 10.1MB)
# 테스트 8 〉	통과 (0.36ms, 10.3MB)
# 테스트 9 〉	통과 (0.53ms, 10.2MB)
# 테스트 10 〉	통과 (2.14ms, 10.2MB)
# 테스트 11 〉	통과 (0.07ms, 10.3MB)
# 테스트 12 〉	통과 (0.13ms, 10.2MB)
# 테스트 13 〉	통과 (0.09ms, 10.2MB)
# 테스트 14 〉	통과 (0.50ms, 10.4MB)
# 테스트 15 〉	통과 (0.13ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.4MB)
# 테스트 17 〉	통과 (0.97ms, 10.3MB)
# 테스트 18 〉	통과 (1.61ms, 10.3MB)
# 테스트 19 〉	통과 (0.99ms, 10.3MB)
# 테스트 20 〉	통과 (2.35ms, 10.3MB)
# 테스트 21 〉	통과 (2.22ms, 10.3MB)
# 테스트 22 〉	통과 (2.18ms, 10.2MB)
# 테스트 23 〉	통과 (2.16ms, 10.2MB)
# 테스트 24 〉	통과 (2.12ms, 10.2MB)
# 테스트 25 〉	통과 (2.40ms, 10.2MB)
# 테스트 26 〉	통과 (2.20ms, 10.3MB)
# 테스트 27 〉	통과 (2.33ms, 10.3MB)
# 테스트 28 〉	통과 (0.01ms, 10.3MB)
