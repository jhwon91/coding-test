import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
data = list(map(int,input().split()))
diff = []

if N <= K:
	print(0)
	exit()

data.sort()

for i in range(1,len(data)):
	diff.append(data[i] - data[i-1])

# 거리 차이를 정렬하여 가장 큰 K-1개를 제거
diff.sort(reverse=True)

# K-1개의 큰 거리를 제외한 나머지 거리의 합이 최소 거리 합
print(sum(diff[K-1:]))

