def solution(number, limit, power):
	answer = 0
	num_list2=[]

	for num in range(1,number+1):
		num_list=[]
		
		for i in range(1,int(num**(1/2))+1):
			if num % i == 0:
				num_list.append(i)
				if i**2 != num:
					num_list.append(num // i)
		num_list2.append(len(num_list))
	
	for i in range(len(num_list2)):
		if num_list2[i] > limit:
			num_list2[i] = power
		answer += num_list2[i]
		
    
	return answer