import sys
import heapq
input = sys.stdin.readline

INF = float('inf')
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 간선 정보 입력
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))  # (비용, 노드)
    graph[b].append((c, a))  

v1, v2 = map(int, input().split())

# 다익스트라 알고리즘 구현
def dijkstra(start):
    dist = [INF] * (N + 1)  
    dist[start] = 0  
    heap = [(0, start)]  # (비용, 노드)

    while heap:
        currentValue, current_node = heapq.heappop(heap)  # 가장 가까운 노드 선택

        # 이미 처리된 노드면 스킵
        if dist[current_node] < currentValue:
            continue

        # 현재 노드와 연결된 모든 인접 노드 확인
        for next_dist, next_node in graph[current_node]:
            if dist[next_node]> currentValue + next_dist: 
                dist[next_node] = currentValue + next_dist
                heapq.heappush(heap, (dist[next_node], next_node))

    return dist

dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

# 경로 1: 1 -> v1 -> v2 -> N
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
# 경로 2: 1 -> v2 -> v1 -> N
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

# 두 경로 중 더 짧은 거리 선택
result = min(path1, path2)
print(result if result < INF else -1)
