from sys import stdin


def find(a):
    if parent[a] == a:
        return parent[a]
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    root1 = find(a)
    root2 = find(b)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


length, input_len = map(int, stdin.readline().split())
parent = [i for i in range(length+1)]
rank = [0 for i in range(length+1)]

for i in range(input_len):
    operation, first, second = map(int, stdin.readline().split())

    if operation:   # 1이면 확인, 0이면 연결
        if find(first) == find(second):
            print('YES')
        else:
            print('NO')
    else:
        union(first, second)