import sys
import heapq
input = sys.stdin.readline

INF = float('inf')
N, M = map(int,input().split())
K = int(input())
graph = [[] for _ in range(N+1)]
dist = [INF] * (N+1)

for _ in range(M):
	u,v,w = map(int, input().split())
	graph[u].append([w,v])

dist[K] = 0
heap = [[0,K]]

while heap:
	currentValue,currentNode = heapq.heappop(heap)

	if dist[currentNode] != currentValue: continue

	for nextValue,nextNode in graph[currentNode]:
		if dist[nextNode] > currentValue + nextValue:
			dist[nextNode] = currentValue + nextValue
			heapq.heappush(heap, [dist[nextNode], nextNode])

for i in dist[1:]:
	if i == INF:
		print('INF')
	else:
		print(i)