# 10
# 1 5 2 1 4 3 4 5 2 1

import sys
input = sys.stdin.readline
N = int(input())
data = list(map(int,input().split()))
reversedData = data[::-1]

increaseDp = [1] * N
decreaseDp = [1] * N
result = [0] * N
for i in range(1,N):
	for j in range(i):
		if data[i] > data[j]:
			increaseDp[i] = max(increaseDp[i], increaseDp[j]+1) 
		if reversedData[i] > reversedData[j]:
			decreaseDp[i] = max(decreaseDp[i], decreaseDp[j]+1)

decreaseDp.reverse()

for i in range(N):
	result[i] = increaseDp[i] + decreaseDp[i] - 1

print(max(result))