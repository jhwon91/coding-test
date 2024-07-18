def solution(t, p):
    answer = 0
    
    for index in range(len(t)-len(p)+1):
        temp = int(t[index:index+len(p)])
        if int(p) >= temp:
            answer += 1
    return answer