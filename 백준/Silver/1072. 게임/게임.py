import sys
X, Y = map(int, sys.stdin.readline().split())
Z = (Y * 100) // X

def solution(start, end):
	if start > end:
		return -1
	mid = (start + end) //2 # 중간 값
	result = ((Y+mid) * 100) // (X+mid)

	if (result > Z):
		if (((Y+mid-1) * 100) // (X+mid-1) == Z):  # mid 바로 이전의 값에서 승률이 여전히 Z인지 확인
			return mid
		else:
			return solution(start,mid-1)
	else:
		return solution(mid+1,end)

print(solution(0,X))

