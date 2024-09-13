from collections import deque
import sys

input = sys.stdin.read
data = input().splitlines()

count = int(data[0])
commend = data[1:]
result = deque([])
for i in range(count):
	com=commend[i].split()
	if com[0] == 'push':
		result.append(com[1])
	elif com[0] == 'pop':
		if len(result) == 0:
			print(-1)
		else:
			print(result.popleft())
	elif com[0] == 'size':
		print(len(result))
	elif com[0] == 'empty':
		if len(result) == 0:
			print(1)
		else:
			print(0)
	elif com[0] == 'front':
		if len(result) == 0:
			print(-1)
		else:
			print(result[0])
	elif com[0] == 'back':
		if len(result) == 0:
			print(-1)
		else:
			print(result[-1])