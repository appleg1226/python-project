from sys import stdin
import heapq

INF = 1e9
V, E = map(int, stdin.readline().split())  # 정점/간선의 갯수
graph = [[] for _ in range(V)]    # 정점 갯수만큼 초기화

for i in range(E):
    u, v, w = map(int, stdin.readline().split())
    graph[u-1].append([v-1, w])    # 양방향 간선 추가
    graph[v-1].append([u-1, w])

a, b = map(int, stdin.readline().split())    # 반드시 a->b를 거쳐야 한다.


def dijk(start, arrive):
    dist = [INF] * V    # 최단거리는 큰 정수로 초기화한다.
    pq = []      # pq에 간선을 보관한다.
    heapq.heappush(pq, (0, start-1))   # 시작하는 부분 초기화
    dist[start-1] = 0   # 거리도 초기화

    while pq:    # pq에서 가장 짧은 구간을 하나씩 빼서 진행한다.
        cur_dist, cur_pos = heapq.heappop(pq)
        if dist[cur_pos] < cur_dist: continue

        for next_pos, next_dist in graph[cur_pos]:
            next_dist += cur_dist
            if dist[next_pos] > next_dist:    # 기준을 만족하면 dist 갱신하고 pq에 해당 간선 넣기
                dist[next_pos] = next_dist
                heapq.heappush(pq, (next_dist, next_pos))

    return dist[arrive-1]


path1 = dijk(1, a) + dijk(a, b) + dijk(b, V)
path2 = dijk(1, b) + dijk(b, a) + dijk(a, V)

ans = min(path1, path2)    # 두 거리 중 짧은 거리를 찾는다.
    
print(ans if ans < INF else '-1')    # 도착 불가능하면 -1 출력
