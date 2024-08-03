n = int(input())
n_num =list(map(int, input().split()))
m = int(input())
m_num = list(map(int, input().split()))

n_num.sort()

answer = []
for num in m_num:
	start = 0
	end = len(n_num)-1
	
	find_bool = False
	while start <= end:
		mid = start + (end-start) //2
		if n_num[mid] == num:
			find_bool = True
			break
		elif n_num[mid] > num:
			end = mid -1
		else:
			start = mid + 1
	
	if find_bool == True:
		answer.append("1")
	else:
		answer.append("0")
		
print(" ".join(answer))