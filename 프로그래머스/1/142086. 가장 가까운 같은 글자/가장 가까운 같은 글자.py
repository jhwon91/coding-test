def solution(s):
    answer = []
    
    for index in range(len(s)):
        if s[:index].rfind(s[index]) == -1:
            answer.append(-1)
        else:
            answer.append(index - s[:index].rfind(s[index]))
    
    return answer