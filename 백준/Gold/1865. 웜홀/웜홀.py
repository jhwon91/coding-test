import sys

INF = float('inf')
T = int(input())

def df(n, graph):
	dist = [0] * (n + 1)  # 모든 노드를 0으로 초기화

	# N번 반복 (음수 사이클 확인을 위해 한번 더)
	for i in range(n):
		for current_node in range(1, n + 1):
			for nextValue, nextNode in graph[current_node]:
				if dist[nextNode] > dist[current_node] + nextValue:
					dist[nextNode] = dist[current_node] + nextValue
					if i == n-1:  # n번째 반복에서도 갱신이 발생하면 음수 사이클 존재
						return True
	return False

for _ in range(T):
	N, M, W = map(int, input().split())
	graph = [[] for _ in range(N + 1)]

	# 도로 정보 입력
	for _ in range(M):
		S, E, T = map(int, input().split())
		graph[S].append((T, E))
		graph[E].append((T, S))

	# 웜홀 정보 입력
	for _ in range(W):
		S, E, T = map(int, input().split())
		graph[S].append((-T, E))

	if df(N, graph):
		print("YES")
	else:
		print("NO")