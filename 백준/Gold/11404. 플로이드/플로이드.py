import sys

INF = float('inf')
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
	graph[i][i] = 0

for _ in range(m):
	a,b,c = map(int, input().split())
	graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
	for i in range(1, n+1):
		for j in range(1, n+1):
			if graph[i][j] > graph[i][k] + graph[k][j]:
				graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1, n+1):
    print(' '.join(map(str, graph[i][1:n+1])))