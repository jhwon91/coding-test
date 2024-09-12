import sys

input = sys.stdin.read
data = input().splitlines()

originData = data[0]
commend = data[2:]

leftArray = list(originData)
rightArray = []

for com in commend:
	if com[0] == "L":
		if leftArray:
			rightArray.append(leftArray.pop())
	elif com[0] == "D":
		if rightArray:
			leftArray.append(rightArray.pop())
	elif com[0] == "B":
		if leftArray:
			leftArray.pop()
	elif com[0] == "P":
		leftArray.append(com[2])

if rightArray:
	rightArray.reverse()

print("".join(leftArray)+"".join(rightArray))