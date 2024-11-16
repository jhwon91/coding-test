
def solution(answers):
    answer = []
    su1 = [1, 2, 3, 4, 5]
    su2 = [2, 1, 2, 3, 2, 4, 2, 5]
    su3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0,0,0]
    
    for i in range(len(answers)):
        if su1[i % len(su1)] == answers[i]:
            scores[0] += 1
        if su2[i % len(su2)] == answers[i]:
            scores[1] += 1
        if su3[i % len(su3)] == answers[i]:
            scores[2] += 1
    
    max_score = max(scores)  
    answer = [i + 1 for i, score in enumerate(scores) if score == max_score]  
    
    return answer