def solution2(data, info):
	N, M, start = data
	graph = [[] for _ in range(N + 1)]
	visited = [0 for _ in range(N + 1)]
	order = 1 

	for i,j in info:
		graph[i].append(j)
		graph[j].append(i)

	for i in range(len(graph)):
			graph[i].sort()

	stack = [start]
	while stack:
		node = stack.pop()

		if visited[node] == 0:
			visited[node] = order
			order += 1

		for nextNode in reversed(graph[node]):
			if visited[nextNode] == 0:
				stack.append(nextNode)

	return visited[1:]

import sys
input = sys.stdin.readline

info = list(map(int,input().split()))
data = [list(map(int,input().split())) for _ in range(info[1])]
result = solution2(info,data)
for i in result:
	print(i)