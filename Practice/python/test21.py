import sys
input = sys.stdin.readline

N, M = map(int,input().split())
datas = list(map(int,input().split()))
result = 0

# 나무 높이를 정렬
datas.sort()

start = 1
end = datas[-1]

while start <= end:
	mid = (start + end)//2
	total = 0
	
	for data in datas:
		if mid < data:
			total += data - mid
	
	if total >= M:
		result = mid 
		start = mid + 1
	else  :
		end = mid - 1

print(result)

