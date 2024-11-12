import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
	data.append(int(input()))

if N == 1:
	print(0)
	exit()

count = 0
data.reverse()

for i in range(1,len(data)):
	while data[i-1] <= data[i]:
		data[i] -= 1
		count += 1
		if data[i] == 0:
			break

print(count)
