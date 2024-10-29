
def solution1(t, cases):
	answer = []
	for i in range(t):
		case = cases[i]	
		start = 1
		end  = case
		result = 0

		while(start <= end):
			mid = (start + end)//2
			if ((mid * (mid + 1)) // 2 <= case):
				start = mid + 1
				result = max(mid, result)
			else: 
				end = mid - 1

		answer.append(result)
	return answer


def solution2(T, cases):
    results = []
    for N in cases:
        current_jump_distance = 1
        count = 1  # 첫 번째 징검다리 밟기
        total_distance = 1
        
        while total_distance + (current_jump_distance + 1) <= N:
            current_jump_distance += 1
            total_distance += current_jump_distance
            count += 1
        
        results.append(count)
    return results



if __name__ == "__main__":
	import time
	import datetime

	import sys
	input = sys.stdin.readline

	T = int(input())
	CASES = [int(input()) for _ in range(T)]

	start = time.time()

	#solution
	sol = solution1(T,CASES)

	for i in sol:
		print(i)

	sec = time.time() - start

	times = str(datetime.timedelta(seconds=sec))
	short = times.split('.')[0]
	print(f"{times} sec")
	print(f"{short} sec")