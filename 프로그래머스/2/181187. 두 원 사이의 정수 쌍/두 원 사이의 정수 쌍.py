import math


def solution(r1, r2):
    answer = 0
    
    for x in range(1, r2+1):
        r1_y = 0.0
        r2_y = 0.0
        if x <= r1:
            r1_y = math.ceil(math.sqrt((r1**2) - (x**2)))
        r2_y = math.floor(math.sqrt((r2**2) - (x**2)))
        
        answer += r2_y - r1_y + 1
    
    answer *= 4
    return answer