import sys 

INF = float('inf')  
input = sys.stdin.readline  

N, M = map(int, input().split())
# 그래프를 INF로 초기화 (N+1 x N+1 크기, 1-index 사용)
graph = [[INF] * (N+1) for _ in range(N+1)]

# 자기 자신으로 가는 거리는 항상 0으로 설정
for i in range(1, N+1):
    graph[i][i] = 0

# 친구 관계 입력 처리
# a와 b가 친구이면 graph[a][b]와 graph[b][a]를 1로 설정 (양방향 그래프)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드-와샬 알고리즘 수행
# 중간 노드 k를 거쳐가는 경우를 고려하며 모든 쌍의 최단 거리를 갱신
for k in range(1, N+1):  # 중간 노드
    for j in range(1, N+1):  # 시작 노드
        for i in range(1, N+1):  # 종료 노드
            # j에서 i로 직접 가는 거리보다 j -> k -> i로 가는 거리가 더 짧으면 갱신
            if graph[j][i] > graph[j][k] + graph[k][i]:
                graph[j][i] = graph[j][k] + graph[k][i]

temp = INF  
result = 0  

for i in range(1, N+1):
    eachSum = sum(graph[i][1:])
    if eachSum < temp:
        temp = eachSum
        result = i

print(result)

