from sys import stdin

"""
각 나무의 길이가 주어져있고, 나무를 일정 높이에서 잘라서 그 위의 것만 가져가려고 한다.
그 때, 환경보호를 위하여 일정 길이 이상을 자르고, 목표에 최대한 가깝게 자르려고 한다.
이럴 때 최대 높이를 구하는 것이 문제.
"""
def cut_trees():
    n, m = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))

    left, right, ans = 0, max(a), 0
    while left <= right:
        mid = (left + right) // 2

        tree = 0     # 잘리는 나무의 길이를 계산
        for i in range(n):
            if mid < a[i]:
                tree += a[i] - mid

        if tree >= m:     # 목표보다 많으면 높이를 늘리고(어쨌든 문제는 해결이니까 답은 저장해놓는다)
            ans = mid
            left = mid + 1
        elif tree < m:    # 목표보다 적으면 높이를 낮춘다
            right = mid - 1

    print(ans)


if __name__ == "__main__":
    cut_trees()