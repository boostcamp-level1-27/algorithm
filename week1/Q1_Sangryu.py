# 8/17
# programmers.co.kr
# 삼각달팽이
# 정수 n이 매개변수로 주어집니다. 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로
# 달팽이 채우기를 진행한 후, 첫 행부터 마지막 행까지 모두 순서대로 합친
# 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

def solution(n):
    row, col, ans = -1, 0, 1
    tri_list = [[0] * i for i in range(1, n + 1)]

    for i in range(n):
        for _ in range(n-i):
            if i % 3 == 0:
                row += 1
            elif i % 3 == 1:
                col += 1
            else:
                row -= 1
                col -= 1
            tri_list[row][col] = ans
            ans += 1

    return sum(tri_list, [])


# 테스트 1 〉	통과 (0.01ms, 10.4MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (1.15ms, 10.8MB)
# 테스트 5 〉	통과 (1.20ms, 10.8MB)
# 테스트 6 〉	통과 (1.25ms, 10.9MB)
# 테스트 7 〉	통과 (2269.08ms, 57MB)
# 테스트 8 〉	통과 (2235.31ms, 57.7MB)
# 테스트 9 〉	통과 (1511.29ms, 58.7MB)
