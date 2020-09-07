from sys import stdin
import sys
sys.setrecursionlimit(10**6)


def double_sort():
    N = int(stdin.readline())
    A = [stdin.readline().rstrip().split() for i in range(N)]     # [[num, name], [num, name], ...]
    A_ = sorted(A, key=lambda x: int(x[0]))    # num을 기준으로 정렬

    # A2 = sorted(A, key=lambda x: (int(x[0]), x[1]))    # num 다음 name으로 정렬

    [print(i[0], i[1]) for i in A_]


if __name__ == "__main__":
    double_sort()