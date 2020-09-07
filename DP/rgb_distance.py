from sys import stdin

"""
N은 집의 갯수
그리고 집의 갯수 N은 각각 R,G,B 새 개의 값을 가진다. 
두 번째줄부터 시작한다.

두 번째 집부터 R, G, B 각 색으로 칠했을 경우 
전 줄에서 칠한 색을 확인하고, 그 최솟값도 확인할 수 있다

"""


def rgb_distance():
    N = int(stdin.readline())
    costs = []
    for i in range(N):
        one_line = list(map(int, stdin.readline().split()))
        costs.append(one_line)

    dists = [costs[0]]

    for i in range(1, N):  # 순차적으로 갱신한다.
        Rmin = min(dists[i - 1][1], dists[i - 1][2]) + costs[i][0]
        Gmin = min(dists[i - 1][0], dists[i - 1][2]) + costs[i][1]
        Bmin = min(dists[i - 1][0], dists[i - 1][1]) + costs[i][2]
        dists.append([Rmin, Gmin, Bmin])

    print(min(dists[N-1]))


"""
위와 비슷한 문제
한번에 계단을 하나 또는 두개를 오를 수가 있다.
T에는 계단의 수. cost[]에는 각 계단을 오를 때의 점수를 입력받는다.
그렇게 해서 가장 높은 점수를 받을 수 있는 경우의 수를 구하는 문제다.

4번째부터 시작하는데, 2개 전에서 올라온 경우와, 1개 전에서 올라온 경우의 최댓값을 구하면 된다.
"""

def stairs():
    T = int(stdin.readline())

    cost = [0] * 301
    scores = [0] * 301

    for i in range(T):
        cost[i + 1] = int(stdin.readline())

    scores[1] = cost[1]
    scores[2] = cost[1] + cost[2]
    scores[3] = max(cost[1] + cost[3], cost[2] + cost[3])

    for i in range(4, T + 1):
        scores[i] = max(scores[i - 2] + cost[i], scores[i - 3] + cost[i - 1] + cost[i])

    print(scores[T])


if __name__ == "__main__":
    rgb_distance()
