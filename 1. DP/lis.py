from sys import stdin
from bisect import bisect_left  # 이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다

"""
유명한 가장 긴 증가하는 부분수열 문제다.
예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
T는 숫자의 갯수, A는 숫자의 배열을 입력받는다.
아래 알고리즘을 진행했을 경우 결과 dp 배열은 A = {0, 1, 2, 1, 3, 2, 4} 가 되어, 답은 4가 된다.
"""

def lis():
    T = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))

    cost = [0] + A
    dp = [0] * (len(cost))

    dp[1] = 1

    for i in range(2, T + 1):
        max_score = 0
        for j in range(1, i):
            if cost[i] > cost[j]:
                max_score = max(max_score, dp[j])
        dp[i] = max_score + 1
    print(dp)
    print(max(dp))


"""
두 번째 방법은 nlog(n)의 시간복잡도를 가지는 성능이 향상된 방법이다.
반복은 딱 배열만큼 진행하며
하나의 dp배열을 bisect를 이용하여 채우는 방식을 이용한다.
"""
def lis2():
    T = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))

    dp = []

    for idx, i in enumerate(A):     # O(n)의 시간 복잡도!!

        k = bisect_left(dp, i)  # 자신이 들어갈 위치 k를 찾는다. O(logn)의 복잡도.
        if len(dp) <= k:  # i가 가장 큰 숫자라면 뒤로 붙인다.
            dp.append(i)
        else:
            dp[k] = i  # 그렇지 않으면 자신보다 큰 수 중 최솟값과 대체
        print("{0}: {1}".format(idx, dp))

    print(len(dp))



if __name__ == "__main__":
    lis2()