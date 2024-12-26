import sys, heapq

INF = float('inf')
input = sys.stdin.readline
N, M, X = map(int, input().split())

# 그래프(정방향)와 그래프(역방향) 초기화
graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    # graph[a]에 (비용, 도착지) 형태로 추가
    graph[a].append([c, b])
    # reverse_graph[b]에 (비용, 시작지) 형태로 추가 (역방향)
    reverse_graph[b].append((c, a))

def dijkstra(start, adj):
    """
    다익스트라 알고리즘으로 start부터 다른 모든 노드까지의
    최단 거리를 계산하여 dist 리스트로 반환한다.
    
    adj: 인접 리스트(그래프), 정방향이든 역방향이든 사용 가능
    """
    dist = [INF] * (N+1)
    dist[start] = 0  
    heap = [[0, start]]

    while heap:
        currentValue, currentNode = heapq.heappop(heap)

        if dist[currentNode] < currentValue:continue

        for nextValue, nextNode in adj[currentNode]:
            if dist[nextNode] > currentValue + nextValue:
                dist[nextNode] = currentValue + nextValue
                heapq.heappush(heap, [dist[nextNode], nextNode])

    return dist

# 1. X에서 시작하는 다익스트라(정방향) -> X -> i 최단거리
dist_from_X = dijkstra(X, graph)

# 2. X에서 시작하는 다익스트라(역방향) -> X -> i(역그래프) = i -> X(원본)
dist_to_X = dijkstra(X, reverse_graph)

# 모든 마을 i(1~N)에 대해 (i -> X) + (X -> i) 최단거리 계산
result = 0
for i in range(1, N+1):
    # i -> X 거리는 dist_to_X[i], X -> i 거리는 dist_from_X[i]
    cost = dist_to_X[i] + dist_from_X[i]
    # 그 중 가장 오래 걸리는 시간
    if cost > result:
        result = cost

# 결과 출력
print(result)
