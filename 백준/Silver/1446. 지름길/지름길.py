import sys
import heapq

INF = float('inf')
input = sys.stdin.readline
N, D = map(int,input().split())
graph = [[] for _ in range(D+1)]
dist = [INF] * (D+1)

# 지름길 정보를 그래프에 추가
for _ in range(N):
	a,b,c = map(int,input().split()) # 시작점, 끝점, 거리
	if b <= D: # 지름길의 끝점이 D를 넘지 않는 경우에만 추가
		graph[a].append([c,b]) # 비용, 노드

# 기본 도로 추가
for i in range(D):
    graph[i].append([1, i + 1])  # 거리 1로 연결

heap = [[0,0]]
dist[0] = 0

while heap:
	currentValue, currentNode = heapq.heappop(heap)

  # 이미 처리된 노드의 거리값이 더 작다면 무시 
	if dist[currentNode] < currentValue: continue

	for nextValue, nextNode in graph[currentNode]:
		if dist[nextNode] > nextValue + currentValue:
			dist[nextNode] = nextValue + currentValue
			heapq.heappush(heap,(dist[nextNode], nextNode))

print(dist[-1])


