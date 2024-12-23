import sys, heapq

input = sys.stdin.readline

INF = float('inf')
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [INF] * (N+1)

for _ in range(M):
	a,b,c = list(map(int, input().split()))
	graph[a].append([c,b])
	graph[b].append([c,a])

heap = [[0,1]]
dist[1] = 0

while heap:
	currentValue, currentNode = heapq.heappop(heap)

	if dist[currentNode] < currentValue : continue

	for nextValue, nextNode in graph[currentNode]:
		if dist[nextNode] > currentValue + nextValue:
			dist[nextNode] = currentValue + nextValue
			heapq.heappush(heap, [dist[nextNode], nextNode])

print(dist[N])