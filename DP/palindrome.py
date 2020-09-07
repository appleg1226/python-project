from sys import stdin
import sys
sys.setrecursionlimit(10**6)

# a, b, c = map(int, stdin.readline().split())
# d = int(stdin.readline())
# a_list = list(map(int, stdin.readline().split()))

"""
팰린드롬은 앞으로 보나, 뒤로 보나 같은 배열을 말한다.
0 1 2 1 3 1 2 1  에서
121, 131, 21312 가 팰린드롬이다.
"""
def palindrome():
    N = int(stdin.readline())         # 수열의 크기
    nums = [0] + list(map(int, stdin.readline().split()))     # 주어진 숫자의 배열

    M = int(stdin.readline())         # 질문의 갯수(팰린드롬이 맞는가)
    se = [list(map(int, stdin.readline().split())) for i in range(M)]      # [a, b] 의 배열의 쌍으로 받는다. 해당 부분배열이 팰린드롬인지 확인

    dp = [[0 for i in range(2001)] for j in range(2001)]   # 이차원 dp 배열로 진행. dp[a][b]는 a~b가 팰린드롬이 맞는가에 대한 boolean 배열

    for i in range(1, N + 1):   # 길이가 1인 구간은 모두 팰린드롬
        dp[i][i] = 1

    for i in range(1, N):       # 길이가 2인 구간체크. 인접한 수가 같으면 팰린드롬
        if nums[i] == nums[i + 1]:
            dp[i][i + 1] = 1

    # 0 1 2 1 3 1 2 1
    # 처음엔 3개짜리 팰린드롬을 체크한다.
    # 다음엔 4개짜리 팰린드롬을 체크한다.
    # ... 마지막엔 7개짜리(i의 최대가 4) 팰린드롬을 체크한다.
    for i in range(N - 2):  # i는 간격
        for j in range(2, N - i):  # j는 시작점
            if dp[j][j + i] and (nums[j - 1] == nums[j + i + 1]):
                dp[j - 1][j + i + 1] = 1

    for i in se:
        print(dp[i[0]][i[1]])



if __name__ == "__main__":
    palindrome()