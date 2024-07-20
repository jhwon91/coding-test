def solution(s):
	answer = 0
	count1=0
	count2=0
	
	for s_sub in s:
			if count1 == count2:
					answer += 1
					count1 = 0
					count2 = 0
			if count1 == 0 and count2 == 0:
					s1 = s_sub
			if s1 == s_sub:
					count1 += 1
			else:
					count2 += 1


	return answer
