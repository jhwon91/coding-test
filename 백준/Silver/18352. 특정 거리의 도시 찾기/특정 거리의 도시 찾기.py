import sys
from collections import deque
input = sys.stdin.readline

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
N,M,K,X = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]
count = 0

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for i,j in data:
	graph[i].append(j)
	# graph[j].append(i)


q = deque([(X, count)])
visited[X] = True
result = []

while q:
	currentNode, currentCount = q.popleft()

	if currentCount == K:
		result.append(currentNode)

	for nextNode in graph[currentNode]:
		if not visited[nextNode]:
			visited[nextNode] = True
			q.append((nextNode, currentCount + 1))

result.sort()

if len(result) == 0:
	print(-1)
else:
	for i in result:
		print(i)