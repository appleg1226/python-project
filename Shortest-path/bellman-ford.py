from sys import stdin
INF = 1e9

N, M = map(int, stdin.readline().split())   # 도시 갯수 / 버스 갯수
graph = [list(map(int, stdin.readline().split())) for i in range(M)]   # start, end, weight 3개를 받는다.
dist = [INF] * N


dist[0] = 0
loop = False

for i in range(N):    # N개의 간선 갯수만큼 실행
    for j in range(M):    # 각 버스 노선을 한 번씩 업데이트
        cur = graph[j][0] -1
        next = graph[j][1] -1
        w = graph[j][2]

        if dist[cur] != INF and dist[next] > dist[cur] + w:
            dist[next] = dist[cur] + w
            if i == N-1:        # 마지막 루프는 음수 루프를 찾는데 사용되는데, 업데이트가 되었으므로 true
                loop = True


if loop:
    print('-1')
else:
    for i in range(1, N):
        if dist[i] == INF:
            print('-1')
        else:
            print(dist[i])