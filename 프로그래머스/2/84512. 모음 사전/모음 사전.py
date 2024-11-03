def solution(word):
    answer = 0
    
    weights = [781, 156, 31, 6, 1]  # [625+125+25+5+1, 125+25+5+1, 25+5+1, 5+1, 1]
    
    dic = {
        'A': 0,
        'E': 1,
        'I': 2,
        'O': 3,
        'U': 4
    }
    
    for w in range(len(word)):
        answer += dic[word[w]] * weights[w] + 1
    
    return answer