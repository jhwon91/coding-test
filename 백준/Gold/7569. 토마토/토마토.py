import sys
from collections import deque
input = sys.stdin.readline

M,N,H = map(int, input().split())
data = [
	[
		list(map(int,input().split())) for _ in range(N)
	]	for _ in range(H)
]
day = 0
q = deque()

for z in range(H):
	for y in range(N):
		for x in range(M):
			if data[z][y][x] == 1:
				q.append((x,y,z,day))

move = [
	(1,0,0),
	(-1,0,0),
	(0,1,0),
	(0,-1,0),
	(0,0,1),
	(0,0,-1),
]

while q:
	currentX, currentY, currentZ, currentDay = q.popleft()

	for moveX, moveY, moveZ in move:
		nextX =currentX + moveX
		nextY =currentY + moveY
		nextZ =currentZ + moveZ
		if 0 <= nextX < M and 0 <= nextY < N and 0 <= nextZ < H and data[nextZ][nextY][nextX] == 0:
			data[nextZ][nextY][nextX] = 1
			q.append((nextX,nextY,nextZ,currentDay+1))
			day = currentDay+1


for z in range(H):
	for y in range(N):
		for x in range(M):
			if data[z][y][x] == 0:
				print(-1)
				sys.exit()

if day == 0:
	print(0)
else:
	print(day)