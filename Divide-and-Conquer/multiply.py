from sys import stdin
import sys
sys.setrecursionlimit(10**6)

"""
A를 B번 곱한 수를 구하는 문제. 커졌을 경우 C로 나눈 나머지를 출력
a^n 에서 n이 2의 배수일 경우와 아닐 경우로 나뉜다.

짝수: a^16 = a^8 * a^8
홀수: a^15 = a * a^14 = a * a^7 * a^7 

이런 식으로 나눠서 계산하게 된다.
"""
def pow_nums(a, b, c):
    a = a % c

    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 == 0:
        temp = pow_nums(a, b // 2, c)
        return (temp * temp) % c
    else:
        return (a * pow_nums(a, b - 1, c)) % c


if __name__ == "__main__":
    A, B, C = map(int, stdin.readline().split())
    pow_nums(A, B, C)