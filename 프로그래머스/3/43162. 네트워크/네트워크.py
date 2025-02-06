from collections import deque

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False] * n  # 0-based index로 변경

    # 그래프 변환 (인접 행렬 -> 인접 리스트)
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:  # 자기 자신은 제외
                graph[i].append(j)

    # BFS 함수
    def bfs(start):
        q = deque([start])
        visited[start] = True
        
        while q:
            node = q.popleft()
            for nextNode in graph[node]:
                if not visited[nextNode]:
                    visited[nextNode] = True  # 방문 체크를 올바르게 수정
                    q.append(nextNode)

    # BFS 탐색 시작
    for i in range(n):  # 0-based index 사용
        if not visited[i]:  # 방문하지 않은 노드라면 BFS 실행
            bfs(i)
            answer += 1  # 새로운 네트워크 발견

    return answer
