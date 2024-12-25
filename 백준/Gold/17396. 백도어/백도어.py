import sys, heapq

INF = float('inf')
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
dist = [INF] * N

observe = list(map(int, input().split()))

for _ in range(M):
	a,b,c = map(int, input().split())
	graph[a].append([c,b])
	graph[b].append([c,a])

heap = [[0,0]]
dist[0] = 0

while heap:
	currentValue, currentNode = heapq.heappop(heap)
	if dist[currentNode] < currentValue :continue
	if  currentNode != N-1 and observe[currentNode] == 1:continue

	for nextValue, nextNode in graph[currentNode]:
		if dist[nextNode] > currentValue + nextValue:
			dist[nextNode] = currentValue + nextValue
			heapq.heappush(heap, [dist[nextNode], nextNode])

if dist[-1] == INF:
	print(-1)
else:
	print(dist[-1])