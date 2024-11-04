from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]


for _ in range(m):
	s, e = map(int, input().split())
	graph[s].append(e)
	graph[e].append(s)

def BFS(start, end, graph):
	
	q = deque([start])
	visited = [0] * (n+1)
	visited[start] =1

	depth = [-1] * (n + 1)
	depth[start] = 0  # 시작 노드의 촌수는 0
	while q:
		s = q.popleft()
		
		for arg in graph[s]:
			if visited[arg] == 0:
				q.append(arg)
				visited[arg] = 1
				depth[arg] = depth[s] + 1
				
				if arg == end:
					return depth[arg]

	return -1

print(BFS(start,end,graph))