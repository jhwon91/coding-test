import sys
input = sys.stdin.readline

N = int(input())

def solution(num):
	dp = [0] * (num+1)
	
	if 1<= num <4:
		return 1

	dp[1] = 1
	dp[2] = 1
	dp[3] = 1

	for i in range(4,num+1):
		dp[i] = dp[i-3] + dp[i-2]

	return dp[num]

for _ in range(N):
	print(solution(int(input())))
