def solution(n, times):
    left = 1
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) //2
        peopel = 0
        
        for time in times:
            peopel += mid//time
        
        if peopel >= n:
            answer = mid
            right = mid -1
        else:
            left = mid + 1
            
    return answer