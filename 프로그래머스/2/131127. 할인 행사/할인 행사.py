from collections import Counter
def solution(want, number, discount):
    answer = 0
    temp = {}
    
    for w, n in zip(want, number):
        temp[w] = n
    
    for i in range(len(discount)-9):
        change = Counter(discount[i:i+10])
        for key in temp:
            if temp[key] - change[key] > 0:
                break
        else:
            answer += 1
        
    return answer