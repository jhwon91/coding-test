def solution(distance, rocks, n):
    answer = 0
    
    rocks.append(distance)
    rocks.sort()
    
    left = 0
    right = distance

    while left <= right:
        mid = (left + right) //2
        prev = 0
        removeRockCount = 0
        
        for rock in rocks:
            diff = rock - prev
            if diff < mid:
                removeRockCount += 1
            else:
                prev = rock
        
        if removeRockCount > n:
            right = mid -1
        else:
            answer = mid
            left = mid + 1
    return answer