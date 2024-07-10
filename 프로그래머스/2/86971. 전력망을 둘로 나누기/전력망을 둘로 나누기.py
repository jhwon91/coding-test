from collections import deque

def BFS (start, graph, visited, check_link):
    q = deque([start])
    visited[start] = True
    cnt = 1
    while q:
        s = q.popleft()
        for adj_v in graph[s]:
            if visited[adj_v] == False and check_link[start][adj_v]:
                q.append(adj_v)
                visited[adj_v] = True
                cnt += 1
    return cnt
def solution(n, wires):
    answer = n -2 
    
    check_link = [[True]*(n+1) for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]

    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
    
    for s, e in wires:
        visited = [False]*(n+1)
        check_link[s][e] = False
        cnt_s = BFS(s, graph, visited, check_link)
        cnt_e = BFS(e, graph, visited, check_link)
        check_link[s][e] = True
        
        answer = min(answer, abs(cnt_s- cnt_e))
            
    return answer