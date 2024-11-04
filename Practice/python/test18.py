def solution1(data, info):
	N, M, start = data
	graph = [[] for _ in range(N + 1)]
	visited = [0 for _ in range(N + 1)]
	order = 1 

	for i,j in info:
		graph[i].append(j)
		graph[j].append(i)

	for i in range(len(graph)):
			graph[i].sort()

	def dfs(node):
		nonlocal order
		visited[node] = order
		order += 1

		for next_node in graph[node]:
				if visited[next_node] == 0: 
						dfs(next_node)
					

	dfs(start)
	return visited[1:]


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



if __name__ == "__main__":
	import time
	import datetime
	import sys
	input = sys.stdin.readline

	info = list(map(int,input().split()))
	data = [list(map(int,input().split())) for _ in range(info[1])]

	start = time.time()

	result = solution1(info,data)
	for i in result:
		print(i)

	sec = time.time() - start

	times = str(datetime.timedelta(seconds=sec))
	short = times.split('.')[0]
	print(f"{times} sec")
	print(f"{short} sec")