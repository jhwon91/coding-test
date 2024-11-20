def solution(n, wires):
    answer = 100000
    tempCnt = 0
    graph = [[] for _ in range(n+1)]
    
    for i,j in wires:
        graph[i].append(j)
        graph[j].append(i)
    
    for v1, v2 in wires:
        visited = [False] * (n + 1)
        
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        tempCnt=abs(dfs(v1,graph,visited) - dfs(v2,graph,visited))
        answer = min(answer, tempCnt)
        
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    return answer


def dfs(currentNode, graph, visited):
    visited[currentNode] = True
    count = 1
    
    for i in graph[currentNode]:
        if not visited[i]:
            count += dfs(i, graph,visited)
            
    return count