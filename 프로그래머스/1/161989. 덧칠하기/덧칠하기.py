def solution(n, m, section):
    answer = 0
    area = 0
    section.sort()
    
    for num in section:
        if(area < num):
            answer += 1
            area = num + (m - 1)
    return answer