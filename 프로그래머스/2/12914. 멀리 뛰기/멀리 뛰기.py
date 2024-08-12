def solution(n):
    answer = 0
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    temp = [0,1,2]
    for i in range(3,n+1):
        temp.append(temp[i-1] + temp[i-2])
    
    answer = temp[-1] % 1234567
    
    return answer