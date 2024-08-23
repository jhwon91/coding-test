from collections import deque

def solution(board):
	answer = 0
	
	max_row = len(board)
	max_col = len(board[0])


	visited = [[False] * max_col for _ in range(max_row)]

	for i in range(max_row):
		for j in range(max_col):
			if board[i][j] == "R":
				start = (i,j)
				visited[i][j] = True
				q = deque([(i,j,0)])

	#상하좌우
	dy = [1,-1,0,0]
	dx = [0,0,-1,1]

	while q:
		y, x , move = q.popleft()

		if board[y][x] == "G":
			return move
		
		for k in range(4):
			cy = y
			cx = x
			while 0<= cy + dy[k] < max_row and 0<= cx + dx[k] < max_col and board[cy + dy[k]][cx + dx[k]] != "D":
				cy += dy[k]
				cx += dx[k]
			if visited[cy][cx] == False:
				visited[cy][cx] = True
				q.append((cy,cx,move+1))

	return -1
