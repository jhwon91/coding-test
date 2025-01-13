import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
	a,b, value = map(int, input().split())
	graph[a].append([b,value])
	graph[b].append([a,value])

def BFS(s, e):
	visited = [False] * (N+1)
	visited[start] = True
	q = deque([[s, 0]])  
	
	while q:
		currentNode, value = q.popleft()
		if currentNode == e: 
			return value

		for nextNode, nextValue in graph[currentNode]:
			if not visited[nextNode]:
				visited[nextNode] = True
				q.append([nextNode, nextValue + value])
	return 0

for _ in range(M):
	start, end = map(int, input().split())
	print(BFS(start, end))