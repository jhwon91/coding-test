import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))
dp = data.copy()

for i in range(1,N):
	for j in range(i):
		if data[i] > data[j]:
			dp[i] = max(dp[i], dp[j] + data[i])

print(max(dp))


