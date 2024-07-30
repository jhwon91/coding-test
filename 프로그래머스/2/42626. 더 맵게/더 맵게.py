import heapq
def solution(scoville, K):
	answer = 0
	heapq.heapify(scoville) #리스트를 heapq로 변환

	while scoville[0] < K:
			if len(scoville) >= 2:
				min1=heapq.heappop(scoville)
				min2=heapq.heappop(scoville)

				new_value = min1 + (min2*2)
				heapq.heappush(scoville, new_value)

				answer += 1
			else:
				answer = -1
				break

	return answer