from sys import stdin
import sys
sys.setrecursionlimit(10 ** 6)

row = [0] * 15
result = 0

def n_queen_problem():
    n = int(stdin.readline())
    n_queen(0, n)


def n_queen(n, num):
    global result

    if n == num:
        result += 1
    else:
        for i in range(num):
            row[n] = i
            if promising(n):
                n_queen(n + 1, num)


def promising(n):
    for i in range(0, n):
        # 새로운 퀸과 기존의 퀸이 같은 행에 있거나 대각선에 있을 경우
        if row[i] == row[n] or abs(row[i] - row[n]) == (n - i):
            return False
    return True


if __name__ == "__main__":
    n_queen_problem()
    print(result)