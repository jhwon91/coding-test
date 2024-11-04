import sys
from collections import deque

input= sys.stdin.readline
info = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(info[1])]

def solution(info, data):
	N,M,start = info
	graph = [[] for _ in range(N + 1)]
	visited  = [0 for _ in range(N + 1)]
	order = 1

	for i,j in data:
		graph[i].append(j)
		graph[j].append(i)
	
	for i in range(len(graph)):
		graph[i].sort()

	q = deque([start])
	visited[start] = order 
	order += 1
	
	while q:
		node = q.popleft()

		for next_node in graph[node]:
			if visited[next_node] == 0:
				q.append(next_node)
				visited[next_node] = order 
				order += 1

	return visited[1:]

result = solution(info,data)
for i in result:
	print(i)

