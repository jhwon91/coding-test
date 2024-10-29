

import sys
input = sys.stdin.readline

T = int(input())
CASES = [int(input()) for _ in range(T)] 

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

sol = solution1(T,CASES)
for i in sol:
	print(i)