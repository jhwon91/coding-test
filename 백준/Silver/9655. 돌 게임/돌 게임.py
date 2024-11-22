
import sys
input = sys.stdin.readline

N = int(input())

dp = [""] * (N+1)
dp[1] = "SK"
if N >= 2:
		dp[2] = "CY"  
if N >= 3:
		dp[3] = "SK"  

for i in range(4, N+1):
	if dp[i-1] == "CY" or dp[i-3] == "CY":
		dp[i] = "SK"
	else:
		dp[i] = "CY"
	
print(dp[N])