import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N + 1)]  

for i, j in data:
    graph[i].append(j)  
    graph[j].append(i)  

# BFS를 통해 한 사용자의 케빈 베이컨 수를 계산하는 함수
def bfs(start):
    total = 0  # 케빈 베이컨 수 합계
    visited = [False] * (N + 1)  # 방문 여부를 기록
    q = deque([(start, 0)])  # (현재 노드, 현재 거리)를 큐에 저장
    visited[start] = True  # 시작 노드를 방문 처리

    while q:
        currentNode, currentCount = q.popleft()  # 현재 노드와 거리 꺼내기
        for nextNode in graph[currentNode]:  # 현재 노드에 연결된 친구 탐색
            if not visited[nextNode]:  # 방문하지 않은 친구라면
                visited[nextNode] = True  # 방문 처리
                q.append((nextNode, currentCount + 1))  # 큐에 추가 (거리 + 1)
                total += (currentCount + 1)  # 총 거리 합계에 추가

    return total  # 시작 노드의 케빈 베이컨 수 반환

# 최소 케빈 베이컨 수와 해당 사용자를 기록할 변수 초기화
temp = float("inf")  # 초기값을 무한대로 설정
result = 0  # 결과로 출력할 사용자 번호

# 모든 사용자에 대해 BFS 수행
for i in range(1, N + 1):
    current_bacon = bfs(i)  # 사용자 i의 케빈 베이컨 수 계산
    if current_bacon < temp:  # 현재 사용자의 케빈 베이컨 수가 더 작다면 갱신
        temp = current_bacon
        result = i  # 결과 사용자 번호 업데이트

# 결과 출력 (케빈 베이컨 수가 가장 작은 사용자)
print(result)
