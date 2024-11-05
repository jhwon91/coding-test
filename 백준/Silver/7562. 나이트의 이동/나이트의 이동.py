import sys
from collections import deque
input = sys.stdin.readline

testCase = int(input())

def bfs(l, start, target):
	#x,y
	move = [
		(2, 1), (2, -1), (-2, 1), (-2, -1),
		(1, 2), (1, -2), (-1, 2),(-1, -2)
	]
	count = 0

	visited = [[False] * l for _ in range(l)]
	targetX, targetY = target[0],target[1]
	q = deque([(start[0], start[1],count)])
	visited[start[0]][start[1]] = True
	
	while q:
		currentX, currentY, currentCount = q.popleft()

		if currentX == targetX and currentY == targetY:
			return currentCount

		for moveX, moveY in move:
			nextX = currentX + moveX
			nextY = currentY + moveY

			if 0 <= nextX < l and 0 <= nextY < l and not visited[nextX][nextY]:
				q.append((nextX, nextY, currentCount + 1))
				visited[nextX][nextY] = True


for _ in range(testCase):
	L = int(input())
	start = list(map(int,input().split()))
	target = list(map(int,input().split()))

	print(bfs(L,start,target))
