from collections import deque
def solution(maps):
    answer = []
    
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    for row in range(len(maps)):
        for col in range(len(maps[row])):
            if maps[row][col] == "X":
                visited[row][col] = True
            if visited[row][col] == True:
                continue
            answer.append(BFS(maps,row,col,visited))
    answer.sort()
    return answer

def BFS(maps, row, col, visited):
    count = int(maps[row][col])
    visited[row][col] = True
    q = deque([(row, col)])
    
    x = [1,0,-1,0]
    y = [0,1,0,-1]
    
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            dx = x[k] + ex
            dy = y[k] + ey
            if 0 <= dy < len(maps) and 0<= dx <len(maps[0]):
                if maps[dy][dx] != "X" and visited[dy][dx] == False:
                    count += int(maps[dy][dx])
                    visited[dy][dx] = True
                    q.append((dy,dx))    
    return count



maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))