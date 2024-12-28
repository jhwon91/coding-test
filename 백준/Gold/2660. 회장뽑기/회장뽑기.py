import sys
input = sys.stdin.readline

INF = float('inf')
N = int(input())
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
	graph[i][i] = 0

while True:
	a, b=map(int, input().split())
	if a == -1:
		break

	graph[a][b] = min(graph[a][b],1)
	graph[b][a] = min(graph[b][a],1)


for k in range(1, N+1):
	for i in range(1, N+1): 
		for j in range(1, N+1):
			if graph[i][j] > graph[i][k] + graph[k][j]:
				graph[i][j] = graph[i][k] + graph[k][j]

score = None
count = 0
result = []
for i in range(1, N+1):
	tempScore = max(graph[i][1:N+1])
	if score is None or score > tempScore:
		score = tempScore

for i in range(1, N+1):
	tempScore = max(graph[i][1:N+1])
	if tempScore == score:
		count +=1
		result.append(i)

print(score,count)
print(' '.join(map(str, result)))