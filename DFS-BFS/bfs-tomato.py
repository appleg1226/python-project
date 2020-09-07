from sys import stdin
from collections import deque

row_move = [1, -1, 0, 0]
col_move = [0, 0, 1, -1]


def bfs(queue_input, matrix_input):
    while queue_input:
        q = queue_input.popleft()
        r = q[0]
        c = q[1]

        now_count = matrix_input[r][c]
        for i in range(4):
            r_next = r + row_move[i]
            c_next = c + col_move[i]
            if r_next >= row or c_next >= col or r_next < 0 or c_next < 0:
                continue

            if matrix_input[r_next][c_next] == 0:
                matrix_input[r_next][c_next] = now_count + 1
                queue_input.append([r_next, c_next])


if __name__ == '__main__':
    queue = deque()
    col, row = map(int, stdin.readline().split())   # 배열 길이 입력

    matrix = [[0]*col for _ in range(row)]

    for i in range(row):
        temp = list(map(int, stdin.readline().split()))   # 각 배열 채우기
        for j in range(col):
            if temp[j] == 1:
                queue.append([i, j])    # 익은 토마토 위치 보관
            matrix[i][j] = temp[j]

    bfs(queue, matrix)

    false_flag = 0
    max_num = 0

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                false_flag = 1
            if matrix[i][j] > max_num:
                max_num = matrix[i][j]

    if false_flag:
        print('-1')
    else:
        print(max_num - 1)