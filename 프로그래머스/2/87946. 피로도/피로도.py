
answer = 0
data = []

def solution(k, dungeons):
    global answer,data
    
    visited = [0] * len(dungeons)
    data = dungeons
    
    dfs(0,k,visited)
    
    return answer

def dfs(count, currnetNum, visited):
    global answer,data
    
    answer = max(answer, count)
    
    for i in range(len(data)):
        if visited[i] == 0 and currnetNum >= data[i][0]:
            visited[i] = 1
            dfs(count+1, currnetNum-data[i][1], visited)
            visited[i] = 0