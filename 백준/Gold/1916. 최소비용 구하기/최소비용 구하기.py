import sys, heapq

INF = float('inf')
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
dist = [INF] * (N+1)

for _ in range(M):
	a,b,c = list(map(int, input().split()))
	graph[a].append([c,b]) # 비용, 노드

start, end = map(int, input().split())

heap= [[0,start]]
dist[start] = 0

while heap:
	currentValue, currentNode = heapq.heappop(heap)

	if dist[currentNode] < currentValue : continue

	for nextValue, nextNode in graph[currentNode]:
		if dist[nextNode] > nextValue + currentValue:
			dist[nextNode] = nextValue + currentValue
			heapq.heappush(heap, [dist[nextNode], nextNode])

print(dist[end])
