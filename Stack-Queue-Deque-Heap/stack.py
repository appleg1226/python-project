from sys import stdin
import sys
sys.setrecursionlimit(10**6)

def parenthesis():
    T = int(stdin.readline())

    for _ in range(T):
        str_input = stdin.readline()

        stk = []
        no_flag = 0
        for i in str_input:
            if i == '(':
                stk.append(i)
            else:
                if not stk:
                    no_flag = 1
                    break
                else:
                    stk.pop()

        if no_flag:
            print('NO')
        elif len(stk) > 0:
            print('NO')
        else:
            print('YES')



if __name__ == "__main__":
    print(1)