import sys

input = sys.stdin.readline

N,K = list(map(int,input().split()))
data = list(map(int,input().split()))

currentNum = sum(data[:K])
maxNum = currentNum

for i in range(K, N):
	currentNum += data[i] - data[i-K]
	maxNum = max(currentNum,maxNum)

print(maxNum)

