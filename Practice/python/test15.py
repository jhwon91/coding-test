
def solution1(x,y,z):
	count = 0
	temp = z

	if (z >= 99):
		return -1

	while(True):
		if (temp != z):
			break
		x, y = x+1, y+1
		temp = (y * 100) // x
		count += 1

	return count


def solution2(start, end):
	if start > end:
		return -1
	mid = (start + end) //2 # 중간 값
	result = ((Y+mid) * 100) // (X+mid)

	if (result > Z):
		if (((Y+mid-1) * 100) // (X+mid-1) == Z):  # mid 바로 이전의 값에서 승률이 여전히 Z인지 확인
			return mid
		else:
			return solution2(start,mid-1)
	else:
		return solution2(mid+1,end)



if __name__ == "__main__":
	import time
	import datetime
	# import sys
	# X, Y = map(int, sys.stdin.readline().split())
	X = 1000000000 
	Y = 470000000

	Z = (Y * 100) // X


	start = time.time()
	# print(solution1(X,Y,Z))
	print(solution2(X,Y))
	sec = time.time() - start

	times = str(datetime.timedelta(seconds=sec))
	short = times.split('.')[0]
	print(f"{times} sec")
	print(f"{short} sec")