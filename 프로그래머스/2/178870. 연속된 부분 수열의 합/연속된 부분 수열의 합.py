def solution(sequence, k):
	answer = []
	end = 1
	start = 0
	answer.extend([0,len(sequence)-1])
	max_sum = sequence[0]
	


	while start < end :
		if max_sum == k and answer[1] - answer[0] > (end-1) - start:
			answer = [start,(end-1)]
			max_sum -= sequence[start]
			start += 1
		elif max_sum >= k:
			max_sum -= sequence[start]
			start += 1
		elif end < len(sequence):
			max_sum += sequence[end]
			end +=1
		else:
			break
	return answer
