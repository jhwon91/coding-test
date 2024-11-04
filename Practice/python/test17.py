
# 먼저, 최소 시간과 최대 시간을 정의해야 합니다. 
# 최소 시간은 1분이고, 최대 시간은 모든 사람이 가장 느린 심사대를 이용하는 경우를 가정했을 때의 시간입니다.
# 이분 탐색을 통해 중간값을 설정하고, 이 시간 내에 모든 사람이 심사를 받을 수 있는지 판단합니다.
# 각 심사대별로 해당 시간 동안 처리할 수 있는 사람의 수를 계산해 전체 합을 구합니다.
# 이 합이 n보다 크거나 같다면, 시간의 상한을 줄이고, 작다면 시간을 늘려가면서 이분 탐색을 반복합니다.
def solution1(n, times):
	answer = 0
	start = 1
	end = max(times) * n
	
	while(start <= end):
		mid = (start + end) //2
		temp = []
		for time in times:
			temp.append(mid//time)
		
		people = sum(temp)
		
		if n <= people:
			answer = mid
			end = mid -1
		else:
			start = mid + 1
	return answer

if __name__ == "__main__":
	import time
	import datetime

	start = time.time()
	n = 6
	times= [7,10]
	print(solution1(n,times))
	sec = time.time() - start

	times = str(datetime.timedelta(seconds=sec))
	short = times.split('.')[0]
	print(f"{times} sec")
	print(f"{short} sec")