from collections import deque

def solution(maps):
	answer = 0
	global n
	global m
	global visited
	
	n = len(maps)
	m = len(maps[0])
	
	visited = [[False] * m for _ in range(n)]
	
	return BEF(maps)

def BEF(maps):
	visited[0][0] = True
	q = deque([(0,0,1)])
	
	direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	while q:
		y, x, cnt = q.popleft()
		
		if y == n-1 and x == m-1:
			return cnt
		
		for dy, dx in direction:
			ny = y + dy
			nx = x + dx
			if 0<= ny < n and 0<= nx < m and maps[ny][nx] == 1 and visited[ny][nx] == False:
					visited[ny][nx] = True
					q.append((ny,nx,cnt+1))
			
	return -1


maps = [
    [1,0,1,1,1],
    [1,0,1,0,1],
    [1,0,1,1,1],
    [1,1,1,0,1],
    [0,0,0,0,1]]	
print(solution(maps))