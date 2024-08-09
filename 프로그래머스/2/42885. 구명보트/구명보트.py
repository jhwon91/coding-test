def solution(people, limit):
    answer = 0
    people.sort()
    
    left = 0
    right = len(people) - 1
    count = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            
        right -= 1
        count += 1
    
    answer = count
    return answer
