from sys import stdin

"""
평범한 배낭 문제는 2차원으로 dp에 접근하는 대표적인 문제다.
2차원으로 생각한 다음, 무엇을 늘릴지 결정하고 순차적으로 확인해본다.
"""
def knapsack_algorithm():
    N, K = map(int, stdin.readline().split())   # 물건 갯수와 최대 무게
    stuff = [[0, 0]]
    knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]    # 배열은 [물건 갯수] * [최대 무게]의 2차원 배열로 0으로 초기화한다.

    for _ in range(N):
        stuff.append(list(map(int, stdin.readline().split())))   # 무게와 가치

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            weight = stuff[i][0]
            value = stuff[i][1]

            if j < weight:    # weight보다 작으면 위의 값을 그대로 가져온다
                knapsack[i][j] = knapsack[i - 1][j]
            else:     # 아니라면 기존 값(윗열)과 새로운 무게(이 물건의 무게를 빼고 다른 물건들의 최댓값에 더하여)를 비교한다.
                knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

        [print(i) for i in knapsack]   # 확인용 배열 출력
        print()

    print(knapsack[N][K])


if __name__ == "__main__":
    knapsack_algorithm()