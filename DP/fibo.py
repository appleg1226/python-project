from sys import stdin


def fibo1(N):    # 단순하게 피보나치 수열을 구하는 방법
    F0, F1 = 0, 1
    for i in range(N):
        F0, F1 = F1, F0 + F1
    return F0


def fibo2(n):   #
    zeros = [1, 0, 1]
    ones = [0, 1, 1]

    if n >= 3:
        for i in range(3, n + 1):
            zeros.append(zeros[i - 1] + zeros[i - 2])
            ones.append(ones[i - 1] + ones[i - 2])

    return [zeros[n], ones[n]]


if __name__ == "__main__":
    N = int(stdin.readline())
    print(fibo1(N))
    print(fibo2(N))
