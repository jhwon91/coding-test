import sys

INF = float('inf')
results = []
T = int(input())

def df(n, graph):
    dist = [INF] * (n + 1)
    dist[1] = 0  # 1번 노드를 시작점으로 설정

    # N-1번 반복
    for _ in range(n - 1):
        for current_node in range(1, n + 1):
            for nextValue, nextNode in graph[current_node]:
                if dist[current_node] != INF and dist[nextNode] > dist[current_node] + nextValue:
                    dist[nextNode] = dist[current_node] + nextValue

    # 음수 사이클 검사
    for current_node in range(1, n + 1):
        for nextValue, nextNode in graph[current_node]:
            if dist[nextNode] > dist[current_node] + nextValue:
                return True  # 음수 사이클 존재

    return False

for _ in range(T):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N + 1)]  # 인접 리스트 초기화

    # 도로 정보 입력
    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((T, E))  # 도로 (양방향)
        graph[E].append((T, S))  # 도로 (양방향)

    # 웜홀 정보 입력
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((-T, E))  # 웜홀 (단방향)

    # 음수 사이클 검사
    if df(N, graph):
        results.append("YES")
    else:
        results.append("NO")

# 결과 출력
print("\n".join(results))
