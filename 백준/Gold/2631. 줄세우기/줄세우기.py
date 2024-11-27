import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
	data.append(int(input()))

dp = [1] * N

for i in range(1,N):
	for j in range(i):
		if data[i] > data[j]:
			dp[i] = max(dp[i],dp[j]+1)

print(N-max(dp))